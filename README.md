# NetAdminAgents

**NetAdminAgents** is an open-source framework for building and deploying Model Context Protocol (MCP)-compliant agents in a **personal AI network**.

This system is designed to support:
- Distributed, local-first agent infrastructure
- Integration with smart home systems like Home Assistant
- Modular agents for weather, calendar, notifications, health, and more
- A self-registering agent directory following the MCP specification

## 🚀 Features
- 🧠 BaseAgent abstraction for standardized agent behavior
- 📚 Directory service for agent discovery and metadata
- 🌐 Event bus compatibility via MQTT and NATS (planned)
- 🛠️ CLI to run and manage agents
- 📄 YAML-based config system

## 📦 Getting Started

```bash
poetry install
python -m NetAdminAgents.cli weather --config agent_config.yaml
```

## 🧩 Architecture
```text
NetAdminAgents/
├── core/        # BaseAgent and context models
├── directory/   # Agent registry and discovery
├── agents/      # Weather, Calendar, Health, etc.
├── cli.py       # CLI entrypoint
└── agent_config.yaml
```

## 📝 License
MIT
