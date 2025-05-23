@description('Location for the resources')
param location string = 'eastus2'

@description('Name of the App Service Plan')
param appServicePlanName string = 'chatbot-app-service-plan'

@description('Name of the Backend App Service')
param backendAppName string = 'chatbot-backend-prasinghal'

@description('Name of the Frontend App Service')
param frontendAppName string = 'chatbot-frontend-prasinghal'

param linuxFxVersion string = 'python|3.11'

@description('OpenAI API Key for the backend')
param openaiApiKey string

@description('OpenAI Base URL for the backend')
param openaiBaseUrl string


resource appServicePlan 'Microsoft.Web/serverfarms@2023-12-01' = {
  name: appServicePlanName
  location: location
  properties: {
    reserved: true
  }
  sku: {
    name: 'B1'
    tier: 'Basic'
  }
  kind: 'linux'
}

// Create the backend App Service
resource backendApp 'Microsoft.Web/sites@2023-12-01' = {
  name: backendAppName
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: linuxFxVersion
      appSettings: [
        {
          name: 'OPENAI_API_KEY'
          value: openaiApiKey
        }
        {
            name: 'OPENAI_BASE_URL'
            value: openaiBaseUrl
        }
      ]
    }
  }
}

resource frontendApp 'Microsoft.Web/sites@2023-12-01' = {
  name: frontendAppName
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: linuxFxVersion
      appSettings: [
        {
          name: 'BACKEND_URL'
          value: 'https://${backendAppName}.azurewebsites.net'
        }
      ]
    }
  }
}

// Outputs for convenience
output backendUrl string = 'https://${backendAppName}.azurewebsites.net'
output frontendUrl string = 'https://${frontendAppName}.azurewebsites.net'
