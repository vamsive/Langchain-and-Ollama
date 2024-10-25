# Ollama Setup Commands

## Commands

### Ollama CLI Cheat Sheet

Quick reference for basic `ollama` commands.

## Commands Overview

- **serve**: Start the Ollama service.
- **create**: Create a new model using a Modelfile.
- **show**: Display details for a specific model.
- **run**: Execute a model.
- **stop**: Stop a running model.
- **pull**: Download a model from a registry.
- **push**: Upload a model to a registry.
- **list**: List all available models.
- **ps**: Show currently running models.
- **cp**: Copy a model to a new location.
- **rm**: Delete a model.
- **help**: Display help for commands.

## Flags

- **-h, --help**: Show help information.
- **-v, --version**: Show version details. 

Use `ollama [command]` to execute any command above.

## Ollama Command Cheat Sheet

A quick reference for commands inside Ollama models:

- **/set**: Set session variables.
- **/show**: Display information about the current model.
- **/load <model>**: Load a specific session or model.
- **/save <model>**: Save your current session.
- **/clear**: Clear the session context.
- **/bye**: Exit the session.
- **/?, /help**: Show help for commands.
- **/? shortcuts**: Display help for keyboard shortcuts.

**Tip:** Use `"""` to start a multi-line message.



## Create a New Model with Custom Settings
    
```bash
ollama create sheldon -f .\mymodelfile.txt
```