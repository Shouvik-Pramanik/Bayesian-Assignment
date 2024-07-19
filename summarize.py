
import click
import openai

@click.command()
@click.option("-t", "--text-file", help="Path to the text file")
@click.argument("text", nargs=-1)
def summarize(text_file, text):
    client = openai.OpenAI(
        base_url='http://localhost:11434/v1/',
        api_key='ollama',  
    )

    if text_file:
        with open(text_file, "r") as f:
            text_to_summarize = f.read()
        summary_title = f"Summary of {text_file}"
    else:
        text_to_summarize = " ".join(text)
        summary_title = "Summary of text pasted"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': text_to_summarize,
            }
        ],
        model='qwen2:0.5b',
    )

    summary = chat_completion.choices[0].message.content

    click.echo(f"{summary_title}\n{summary}")

if __name__ == "__main__":
    summarize()