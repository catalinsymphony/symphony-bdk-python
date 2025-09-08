
def tool(description: str, is_admin: bool = False):
    """
    A decorator to mark a service method as a tool for AI agents.

    :param description: A description of what the tool does. This will be used by the AI to decide when to use
                        the tool.
    :param is_admin: A boolean to indicate if the tool requires admin privileges.
    """

    def decorator(func):
        setattr(func, '_is_tool', True)
        setattr(func, '_tool_description', description)
        setattr(func, '_tool_is_admin', is_admin)
        return func

    return decorator
