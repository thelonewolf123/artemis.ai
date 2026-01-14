# Artemis AI

**A Practical Guide to Building Agentic AI Systems**

Artemis teaches you how to build AI agents from first principles — no magic, no black boxes.

## What You'll Learn

- What LLMs actually are and how they work
- How to talk to models through APIs
- How to give LLMs the ability to take actions (tool calling)
- How to build persistent, multi-user agents
- How to deploy to Telegram and beyond

## Quick Start

```bash
# Clone the repository
git clone https://github.com/thelonewolf123/artemis.ai.git
cd artemis.ai

# Set up environment
export OPENAI_API_KEY=your_key_here

# Install and run
cd backend
pip install -e .
python -m backend.main
```

## Documentation

Full documentation is available at [docs/](./docs) or run locally:

```bash
cd docs
npm install
npm start
```

## Project Structure

```
artemis.ai/
├── docs/       # Interactive documentation (Docusaurus)
└── backend/    # Python implementation
```

## Who Is This For?

- Developers curious about agentic AI
- Engineers who want to understand, not just integrate
- Builders who prefer first principles over frameworks

## License

MIT
