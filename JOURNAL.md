# Development Journal

* 2024-06-01: Setup initial infrastructure: Jupyter + ChromaDB + CLIPS, let's forget about building a web UI for now.
* 2024-06-02: Super naive implementation done. Need to focus on defining clear inputs, outputs & data sanitization next.
* 2024-06-05: Manual cleanup of the scanned files. Gitbrief side-quest. Summarizer for the .txt files.

# To Check

* Using llama3 function calling / tools to call CLIPS?
* Even IF the LLM can execute CLIPS statements, will it be able to keep state like in the REPL?
* Looks like we can put the small dataset completely in the context (± 5k token). Try that vs. RAG?

# Literature

* https://arxiv.org/pdf/2402.12091

# Brainstorming

## Ideas / Questions

* Do current LLM implementations know about the pose-counterpose rule in Yoga? Can they apply it to a flow?
* Can current LLM implementations generate Yoga flows for specific benefits and counter-indications?
* What is the probability that we reach AGI with pure LLM approaches? What about narrow AI?
* Can LLM Routing over many Narrow AI experts mimick a General AI?
* Can injecting symbolic logic into a Narrow AI improve its performance?
* Can injecting symbolic logic into a Narrow AI improve reliability?
* The big gamble: OpenAI seems to bet that Multi-Modal LLMs + Synthetic Data is enough to reach AGI. Is it?
* Are LLMs the new expert systems? Will an AI winter follow?
* IF we find that feeding symbolic logic to an LLM in a way it understands is useful, how do we practically do that?
* Do we even need to bother with formal representations? Can we just get a bunch of experts describe the logic in IF-THEN sentences?
* AGI = MULTI-DOMAIN + AUTO-LEARNING + GENERALIZATION + REASONING
* Current LLM MULTI-DOMAIN: this seems to be working to some extent (GPT4-o)
* Current LLM AUTO-LEARNING: ??? No higher-level learning currently ???
* Current LLM GENERALIZATION: ??? Limited ???
* Current LLM REASONING: Very limited, can't recover from mistakes.
* Isn't it amazing we had these long discussions 20 years ago about trusting Wikipedia vs. a "Real" Encyclopedias & now we're like "Feed all them interwebs to them GPTs, YOLO!"

## Input

 * Do we need to do entity extraction on the input?
 * How to translate input to state / context? Represent it? 
 * KISS: "Given a pos X design a yoga flow Y that contains the pose and is suitable for [contra-indications, desired-effect].
 
    Can you please share your age?
    Have you practiced yoga before? If so, for how long?
    What is your current experience level with yoga (beginner, intermediate, advanced)?
    Do you have any injuries or medical conditions that I should be aware of?
    Are there any physical limitations or restrictions I should consider (e.g., pregnancy, recent surgery, chronic pain)?
    What are your main goals for this session (e.g., relaxation, strength, flexibility, stress relief)?
    Are there specific areas of the body or types of poses you would like to focus on (e.g., backbends, hip openers, inversions)?
    Do you prefer a more dynamic (vinyasa) or static (hatha) practice?
    How long should the flow be?
    Do you have a preferred yoga style (e.g., Ashtanga, Yin, Restorative)?
    Would you like to include meditation or pranayama (breathing exercises)?
    Where will you be exercising (e.g., studio, outdoor, online)?
    What equipment will you have available (e.g., yoga mats, blocks, straps, blankets)?

## Representations

* Dump logic rule + text representation in context? In fine-tuning?

## Expected Output

* Can be as simple as an array of pose-ids" [pose1, pose5, pose6] & feed that to the context?
* Chaining prompts? One for logic, another to create human-readable output?