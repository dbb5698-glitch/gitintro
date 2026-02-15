from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parents[1]))

from util.llm_utils import AgentTemplate

# Add code here
def validate_template_files():
    """Validate that all required template files exist."""
    templates = ['lab04_dm.json', 'lab04_npc.json', 'lab04_enemy.json']
    for template in templates:
        path = Path(__file__).parent.joinpath(template)
        if not path.exists():
            raise FileNotFoundError(f"Template file not found: {template}")
 
# But before here.

def run_console_chat(template_file, agent_name='Agent', **kwargs):
    '''
    Run a console chat with the given template file and agent name.
    Args:
        template_file: The path to the template file.
        agent_name: The name of the agent to display in the console.
        **kwargs: Additional arguments to pass to the AgentTemplate.from_file method.
    '''
    chat = AgentTemplate.from_file(template_file, **kwargs)
    response = chat.start_chat()
    while True:
        print(f'{agent_name}: {response}')
        try:
            response = chat.send(input('You: '))
            # Decide whether the DM selected an encounter and start that agent's chat
            lower = response.lower() if isinstance(response, str) else ''

            # match by name or by descriptive keywords
            if 'kevin' in lower or 'npc' in lower or 'friendly' in lower or 'quest' in lower:
                npc_name = 'Kevin The Lin'
                print(f'{agent_name} selected encounter: {npc_name}')
                npc_template = str(Path(__file__).parent.joinpath('lab04_npc.json'))
                run_console_chat(npc_template, agent_name=npc_name)
                break
            elif 'perry' in lower or 'enemy' in lower or 'hostile' in lower or 'fight' in lower or 'monster' in lower:
                enemy_name = 'Perry the Platypus'
                print(f'{agent_name} selected encounter: {enemy_name}')
                enemy_template = str(Path(__file__).parent.joinpath('lab04_enemy.json'))
                run_console_chat(enemy_template, agent_name=enemy_name)
                break

            # But before here.
        except StopIteration as e:
            break

if __name__ ==  '__main__':
    # start the DM chat, providing the encounters the DM can choose from
    validate_template_files()
    dm_template = str(Path(__file__).parent.joinpath('lab04_dm.json'))
    encounters = 'Kevin The Lin, a Shitty NPC who can offer quests and rewards; and Perry the Platypus, a hostile enemy who wants to fight you.'
    run_console_chat(dm_template, agent_name='DM', encounters=encounters)