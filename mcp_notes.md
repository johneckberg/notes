# MCP

MCP follows a client-server architecture where an MCP host, an AI application like Claude or ChatGPT,  establishes connections to one or more MCP servers. The MCP host accomplishes this by creating one MCP client for each MCP server. Each MCP client maintains a dedicated one-to-one connection with its corresponding MCP server.


Example: A Weather Forecast Service

Let's imagine an existing weather API that needs an API key and a specific latitude and longitude as input. Without MCP, the LLM would need to be given the API key and told to format the request directly.

Instead, You create a simple server with an endpoint like /get-weather. This server handles the details.

## a quick note on LLM tool calling
[Gemini tool calling](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting)
[Chagpt tool calling](https://platform.openai.com/docs/guides/function-calling?api-mode=responses)

You can give a model access to your own custom code through function calling. Tool JSON will be passed in with the system prompt. Based on the system prompt and messages, the model may decide to call these functions. 

MCP is a concrete implementation of tool calling. MCP represents the first major attempt at a “portable tool interface”.The biggest contribution is the standardization of tool as a service IMO it separate the tool supplier and the tool user. Tool calls are your responsibility to write and maintain. In your application it's onto your team to ensure they're up to date, and maintained if the api ever changes. Using a standalone mcp moves that responsibility to the provider and away from your team. Now it's your responsibility to test dozens of broken oss MCP servers and end up writing your own !!


## Now you can do:
Prompt: "What is the weather like in Milwaukee, Wisconsin? Use the /get-weather tool."

Response: The LLM calls the /get-weather endpoint with "Milwaukee, Wisconsin" as a parameter. The wrapper server then:

- Translates "Milwaukee, Wisconsin" to its latitude and longitude.
- Adds the stored API key securely.
- Makes the actual call to the third-party weather API.
- Parses the weather API's JSON response.
- Returns a simple, clean summary to the LLM, like "The current temperature is 68°F and sunny."

## MCP logging
The Model Context Protocol (MCP) provides a standardized way for servers to send structured log messages to clients. Clients can control logging verbosity by setting minimum log levels, with servers sending notifications containing severity levels, optional logger names, and arbitrary JSON-serializable data.