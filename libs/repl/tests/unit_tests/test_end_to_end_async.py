from __future__ import annotations

from blackcat.graph import create_black_cat
from protohello_core.messages import AIMessage, HumanMessage

from protohello_repl.middleware import ReplMiddleware
from tests.unit_tests.chat_model import GenericFakeChatModel


def mul(left: int, right: int) -> int:
    return left * right


async def test_blackcat_with_repl_interpreter() -> None:
    """Basic async test with Repl interpreter."""
    model = GenericFakeChatModel(
        messages=iter(
            [
                AIMessage(
                    content="",
                    tool_calls=[
                        {
                            "name": "repl",
                            "args": {"code": "print(mul(6, 7))"},
                            "id": "call_1",
                            "type": "tool_call",
                        }
                    ],
                ),
                AIMessage(content="The answer is 42."),
            ]
        )
    )

    agent = create_black_cat(
        model=model,
        middleware=[ReplMiddleware(ptc=[mul])],
    )

    result = await agent.ainvoke(
        {"messages": [HumanMessage(content="Use the repl to calculate 6 * 7")]}
    )

    assert "messages" in result
    tool_messages = [msg for msg in result["messages"] if msg.type == "tool"]
    assert [msg.content for msg in tool_messages] == ["42"]
    assert result["messages"][-1].content == "The answer is 42."
    assert len(model.call_history) == 2
    assert (
        model.call_history[0]["messages"][-1].content
        == "Use the repl to calculate 6 * 7"
    )
