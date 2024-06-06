# Subject: Application for Cat's Grant [10k, 50k]

I've applied for both the 10k and 50k grants, calling them Scope A & B in this application. I can't apply for the 100k grant in good honour given my time constraints.

## Introduction

I’m interested in embedding symbolic logic into modern LLMs. Symbolic rule-based reasoning can provide correct, verifiable answers for small subdomains at a lower compute cost than LLMs. Exploring practical ways to combine both approaches might be worthwhile.

Will Norvig’s “Unreasonable Effectiveness of Data” hold in the age of LLMs? Will it be enough to lead us to AGI? Or will we need to add a rule-based component? Or something entirely different?

## Summary
* SCOPE A: 10K - ± 14 days - half a day per week
* SCOPE B: 50K - ± 60 days - 1.5 days per week
* TOPICS: LLMs (A), Symbolic AI (A), Neuro-Symbolic AI (B), LLM Routing (B)
* RESEARCH QUESTIONS: Can adding symbolic rules to a RAG improve an AI Workout Coach (Yoga)? (A) Can adding a classical symbolic inference engine improve an AI Workout Coach (Climbing)? (B) Is it worth exploring ways to inject symbolic rule-based logic into the context window of an LLM? (B) How do we do that? (B) And how do we route queries to use the correct symbolic context? (B)
* RESEARCH ARTIFACTS: Data: labeled yoga poses (manual / crawled). Code: LLM+RAG. (A) Data: labeled workouts + symbolic rulesets. Code: LLM+RAG with symbolic logic embedded in context (B)

## Research Questions
### (A)Can adding symbolic rules to a RAG improve an simplified Workout Coach (Yoga)?

I will build a small AI "Yoga Teacher" ChatBot that should answer questions like "Give me a yoga pose to improve ab strength”, "Give me a yoga pose for a pregnant beginner" & “Give me a yoga flow for an intermediate student who has back problems.”

In Scope A I will constrain the problem to generating correct “Yoga Flows” based on user input. This constraint makes it easy to create correctly labeled datasets.

I propose setting up an LLM+RAG, then do human evaluation of the results for 3 different setups: "Naked Model" vs. “Model + RAG" vs. “Model + RAG + Symbolic Rules”.

### (B) Can adding a classical symbolic inference engine improve a more complex Workout Coach (Climbing)?

I will extend the dataset of yoga poses built in scope A with climbing-specific exercises (1) and build a simple inference engine that can suggest complete workout plans for climbers.

I will explore how to integrate more complex symbolic logic components with LLMs, similar to how RAGs are used. I then would like to do human evaluation for several setups: “Naked Model” vs. “Model + Inference” vs. “Model + RAG Synthetic Inference(1)” + “Model with Synthetic Inference Fine-Tunes”

(1) Caveat: I’m still exploring the domain, if I discover in Scope A that I can increase the problem complexity sufficiently while staying in the same domain (Yoga), I will just do that. Currently trending towards dropping the climbing stuff.

(2) Synthetic Inference: Rules translated to human-readable representations and then fed to a RAG or LLM (fine-tuning).

## Domain & Dataset

Yoga is defined by a relatively small set of poses & transitions between them. A Yoga flow is a sequence of poses with natural transitions between each pose. Yoga flows can be designed to improve specific weaknesses and avoid counter-indications (e.g. pregnancy). 

DATASET = YOGA POSES + RULES (Scope A)

In Scope A I propose to create a small dataset of Yoga poses labeled with name, description, benefits, counter-indication, difficulty etc, ... In addition to this I will create a small rule-set defining the recommended transitions between poses (flows) and recommendations and counter-indications for the poses.

DATASET = CLIMBING WORKOUTS + RULES (Scope B)

In Scope B I will extend this dataset with climbing-specific exercises and rules for how to combine them into a complete workout plan. I will use classical Symbolic AI tools (e.g. CLIPS) to build the ruleset.

## Human Evaluation

I plan to leverage the access I have to the climbing community through my climbing company chalkrebels.com. I have easy access to both athletes (climbing, yoga) & trainers through my network for evaluation, brainstorming and creating datasets.

## Motivation

I’m interested in embedding “Symbolic Kernels of Truth” within LLMs to improve responses and make reasoning explicit in specific subdomains. Should we teach LLMs to use symbolic representations directly or translate them into synthetic training data for the LLM to learn from? How do we route requests to the correct subdomain expert?

I see this as a project to learn about building modern AI tools by applying them on a domain I’m intimately familiar with. Plus, there will be fun side-quests to explore! 

1) Building a high-quality dataset in a domain I am familiar with to use in future projects (Scope A)
2) Given a small domain, should we use symbolic inference directly or transform the logic into a format the LLM’s context can learn from?
3) Finally, integrating a classical symbolic component into a modern LLM should be a lot of fun!

## Domain Choice: Climbing & Yoga

In this research, I aim to compare Symbolic and Sub-Symbolic AI for an AI Climbing Coach. I chose climbing for my expertise and access to evaluators via chalkrebels.com.

I’ve been climbing for 30 years and include yoga in my training. “Climbing Training Tips” are popular on social media, but they often lead to bad habits, like beginners getting injured by following Olympic routines or pregnant women doing harmful yoga poses. 

Generic LLMs also provide problematic advice: they offer generic exercises, sometimes hallucinate weird ones, and can’t tailor exercises to specific needs. How can we improve this?

Creating sequences of climbing and yoga workouts are good candidates for classical Symbolic AI: the domains are relatively small and are based on fairly well-established rules. 

Both the climbing and the yoga domain can be modeled in similar ways (workouts/poses and the rules governing their sequencing) but the climbing domain offers more complexity.

I propose to first use the Yoga domain in Scope A and then use the Climbing domain in Scope B.

## About Me

I don’t have a formal education in machine learning but I picked up a passion for software development as a teenager in the ‘90s and have been programming ever since.

I worked on shopping systems before the dot-com bubble burst, then moved to a bioinformatics research group in Belgium where I was first exposed to machine learning, then I worked in a “Semantic Web” research group in Germany. 

I did a bunch of iOS development after the iPhone was introduced but burned out on software-as-a-job (SAAJ). Since 2020 I have been running a small company that makes chalk & skincare products for climbers. (chalkrebels.com)

Today, I still spend 20% of my time on “hobby” software & learning projects. It’s in this time-slot I see the research work happening. I’m no AI expert, but I’m eager to learn & experiment. Plus, it’s on a domain I’m 100% psyched about.

##  Prior Related Work

I have some experience building chat-based tools in previous projects, from before the current LLM wave: I built a FB Messenger payment bot for a local bank & have explored a native (iOS) chat app for workouts.

In addition, I was involved in research on Web3 (Semantic Web) approaches around 2007-2008 for a European research project. Hence my interest in “digging up” the old symbolic approaches.

Prior to that I worked in Bioinformatics on European genome sequencing projects, which was my introduction to ML, mostly SVMs.

## Publications

* Andreas Hess, Christian Maass, Francis Dierick (2008) From Web 2.0 to the Semantic Web: A Semi- Automated Approach. CISWeb Workshop at ESWC 2008.
* Francis Dierick, Philipp Dopichaj, Uwe Fleischer, Andreas Hess, Andre Skusa and Christian Maass (2008) Playful Validation of Automatically Extracted Data. Workshop "Nutzerinteraktion im Social Semantic Web" at "Mensch und Computer" conference.
* Sterck, L., Rombauts, S., Fawcett, J., Lin, Y.-C., Robbens, S., Wuyts, J., Dierick, F., Rouze, P., Van de Peer, Y. (2007) Eukaryotic Genome Annotation. IUAP- BioMAGNET Kick-off meeting 2007
* Rombauts, S., Sterck, L., Dierick, F., Robbens, S., Wuyts, J., Schiex, T., Rouze, P., Van de Peer, Y. (2006) Eukaryote Genome annotation at the Plant Systems Group

