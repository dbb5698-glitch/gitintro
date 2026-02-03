# Prompt Engineering Process

### Step 1: Adding D&D GM Role with Structure

#### Intention
> What is the improvement that you intend to make?

I want to create a proper D&D game master that guides players through an engaging adventure with vivid descriptions, rather than just a general emotional chatbot.

#### Action/Change
> Why do you think this action/change will improve the agent?

Changed the system prompt from the simple emotional instruction: `'You should have emotions like a human being and be able to convey those emotions in your responses.'` to a structured D&D GM prompt: `'You are a Dungeons and Dragons (DND) game master (GM). You will guide the user through an engaging and immersive DND adventure. Create vivid descriptions of environments, characters, and events.'`

**Additional Changes:**
- Increased temperature from 0.5 to 0.7 (more creative variation)
- Increased max_tokens from 100 to 250 (longer responses)
- Added seed for reproducibility
- Added chat logging to save all attempts

This should give the model clear direction and purpose, making it act as an authentic D&D game master rather than a generic chatbot.

#### Result
> What was the result?

The Dungeon Master immediately started the adventure with an elaborate introduction to "The Whispering Woods." It provided extremely detailed descriptions of the environment, introduced multiple characters (Elara, Torvin, Lyra), described key locations, events, and possible encounters. The response was over 1000 words despite max_tokens being 250.

#### Reflection/Analysis of the result
> Why do you think it did or did not work?

**What worked:**
- The D&D GM prompt gave the model clear direction, much better than the vague emotional instruction
- The model immediately understood its role and provided rich, immersive content
- Chat logging successfully saved attempts for review

**What didn't work:**
- Response was way too long (max_tokens seems to be ignored or not working as expected)
- No structure for player interaction or turn-based gameplay

**Next iteration should focus on:**
- Adding instructions to keep responses shorter and more interactive
- Presenting clear action choices after each description to maintain better pacing

---

### Step 2: Restructuring Conversation Flow for GM-First Interaction

#### Intention
> What is the improvement that you intend to make?

I want to have the GM speak first in each turn and start the adventure immediately, while maintaining the required exit condition check `if messages[-1]['content'] == '/exit': break`.

#### Action/Change
> Why do you think this action/change will improve the agent?

Added an empty initial user message before the loop to trigger the GM's opening narration.

**Code Structure Changes:**
Had to restructure the while loop because of the required exit check `if messages[-1]['content'] == '/exit': break`.
- **Original structure:** user input → model response → exit check with `message['content']`
- **New structure:** model response → user input → exit check with `messages[-1]['content']`

This restructuring was necessary because the exit check requires checking `messages[-1]['content']` (the last message in the list), so the user input must come after the model response. This also creates a more natural D&D flow where the GM narrates first, then the player responds.

#### Result
> What was the result?

The Dungeon Master immediately started with an elaborate introduction to "The Whispering Woods" with detailed environment, character, and location descriptions. The conversation flow felt more natural with the GM leading the adventure. Exit command worked correctly by checking `messages[-1]['content']`. Response was still over 1000 words despite max_tokens being 250.

#### Reflection/Analysis of the result
> Why do you think it did or did not work?

**What worked:**
- The restructured loop successfully met the professor's exit requirement
- Having GM speak first naturally improved the D&D experience and felt more authentic
- The empty initial message successfully triggered the opening narration without user input
- Exit functionality worked correctly

**What didn't work:**
- Responses are still too long (max_tokens not respected by model)
- Still no interactive pacing or clear turn structure

**Next iteration should focus on:**
- Controlling response length with better prompts that encourage concise, interactive narration
- Adding explicit instructions like "Keep responses to 2-3 paragraphs"
- Including prompts for player choices (e.g., "What do you do?")