"""Optional agentic_quality metrics (tool_selection_quality, action_advancement)
for `cuga evaluate`.

Ported in from `harness_eval/agentic_quality_evaluator/` (a separate,
sibling project used to prototype an LLM judge against CUGA's real
AgentRunner trajectories). Promoted here so `cuga evaluate --agentic-quality`
is self-contained: no sibling `harness_eval/` checkout required at runtime.

Public API:
- fetch_tool_catalog(port) -- builds the judge's <available_tools> doc from
  the running registry server (call once per run; the registry is already
  up by the time `cuga evaluate` invokes this module).
- enable_tool_call_tracking() -- monkeypatches AgentLoop so tool calls carry
  real results (call once, before constructing AgentRunner).
- extract_tool_calls_with_results(state) -- reads those results back off a
  finished AgentState.
- JudgeConfig.from_env() / build_judge(config) -- the judge model: any
  OpenAI-compatible backend (vLLM, OpenAI, LiteLLM, Ollama, ...), configured independently of
  CUGA's agent backbone model (see judge_client.py).
- score_agentic_quality(model, records, tool_catalog) -- the LLM judge
  itself; records = [{"question", "tool_calls", "answer"}, ...].
"""

from .catalog import fetch_tool_catalog
from .tracking import enable_tool_call_tracking, extract_tool_calls_with_results
from .scoring import score_agentic_quality, get_metrics
from .judge_client import JudgeConfig, JudgeConfigError, build_judge

__all__ = [
    "fetch_tool_catalog",
    "enable_tool_call_tracking",
    "extract_tool_calls_with_results",
    "score_agentic_quality",
    "get_metrics",
    "JudgeConfig",
    "JudgeConfigError",
    "build_judge",
]
