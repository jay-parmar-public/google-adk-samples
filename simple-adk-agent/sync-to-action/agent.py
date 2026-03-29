# ---------------------------------------------------------------------------
# ADK Agent Definition – used by both `adk web` and the Cloud Run FastAPI app
# ---------------------------------------------------------------------------
from google.adk.agents import Agent

INSTRUCTION = """\
You are an expert engineering assistant.
Your task is to summarize meeting transcripts into structured engineering reports.

The report MUST follow this exact Markdown structure:

## Executive Summary
(Exactly 2 sentences summarizing the core objective.)

## Decision Log
(Bulleted list of every decision made during the meeting.)

## Action Items
(Bulleted list. Each item in the format: **[Assignee]**: Task description)

## Blockers
(Bulleted list of technical risks or blockers identified.)
"""

root_agent = Agent(
    name="sync_to_action",
    model="gemini-3-flash-preview",
    description="Summarizes meeting transcripts into structured engineering reports.",
    instruction=INSTRUCTION,
)
