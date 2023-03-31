import streamlit as st


def _get_state() -> None:
    if 'session_state' not in st.session_state:
        st.session_state['session_state'] = {}
    return st.session_state['session_state']


def __getattr__(name: str):
    state = _get_state()
    if name in state:
        return state[name]
    else:
        return None


def __setattr__(name: str, value) -> None:
    state = _get_state()
    state[name] = value


def __delattr__(name: str) -> None:
    state = _get_state()
    if name in state:
        del state[name]
    else:
        raise AttributeError(f"No such attribute: {name}")
