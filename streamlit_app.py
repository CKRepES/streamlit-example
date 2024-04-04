import openai
import time

# Set your OpenAI API key
api_key = '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'
openai.api_key = api_key

def send_message(message):
    response = openai.Completion.create(
        engine="davinci", 
        prompt=message, 
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to ChatGPT! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        start_time = time.time()
        response = send_message(user_input)
        end_time = time.time()

        print("ChatGPT:", response)
        print("Response time: {:.2f} seconds".format(end_time - start_time))

if __name__ == "__main__":
    main()
