from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Dal Basnet'
model = 'gemma3:270m'
options = {'temperature': 0.7, 'max_tokens': 250}
messages = [{'role':'system', 'content': 'You are a Dungeons and Dragons (DND) game master (GM). '
                                 'You will guide the user through an engaging and immersive DND adventure. '
                                 'Create vivid descriptions of environments, characters, and events. '}
                                 ]



# But before here.
messages.append({'role':'user', 'content':''}) # An empty user message to prompt the model to start responding.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:

  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  print(f'Dungeon Master: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)
  
 
  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

