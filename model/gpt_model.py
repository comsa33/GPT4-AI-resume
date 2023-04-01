import openai


def get_response_from_model(model, temperature, messages):
    response = openai.ChatCompletion.create(
        model=model,
        temperature=temperature,
        messages=messages,
        stream=True,
    )
    return response
