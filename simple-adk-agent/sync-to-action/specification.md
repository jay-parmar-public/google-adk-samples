# Specification: Sync-to-Action Agent
## Goal
Create a single ADK agent that summarizes meeting transcripts into structured engineering reports.

## Technical Requirements
- Framework: Google ADK (Python)
- Model: Gemini 2.0 Flash
- Input: JSON POST request with a "transcript" field.
- Output: Markdown summary with:
  - Executive Summary (2 sentences)
  - Decision Log (Bulleted list)
  - Action Items ([Assignee]: Task)
  - Blockers (Technical risks)

## Deployment Requirement
- Must include a Dockerfile to run on Cloud Run (Port 8080).