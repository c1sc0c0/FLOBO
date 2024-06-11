# Subject: Application for Cat's Grant [50k, 100k](#)

I applied for both the 50k and 100k grants. Although I can’t justify applying for the full 100k grant due to time constraints, I might need to invest in compute resources, which could push the total beyond the 50k base.

## Summary
* SCOPE: 50K + compute - ± 90 days - 2.5 days per week
* TOPICS: LLMs, Symbolic AI, Neuro-Symbolic AI, Benchmarking
* RESEARCH QUESTIONS: 1) Do Large Language Models Understand Logic or Just Mimick Context? (Replication) 2) How does implementation architecture impact correctness & speed of logical inference?
* RESEARCH ARTIFACTS: Code + Data used in replication of Junbin Yan & al. paper. System to benchmark logical correctness & speed of inference.

## Intro
I’m interested in integrating symbolic logic into modern LLMs. Symbolic reasoning offers correct, verifiable answers for small subdomains at lower compute costs than LLMs. However, LLMs are rapidly improving and may be learning logic. 

Before investing effort in integration, we need to benchmark pure transformer-based approaches. This will give us a baseline to compare with future Neuro-Symbolic methods.

I propose replicating Junbin Yan’s paper “Do Large Language Models Understand Logic or Just Mimic Context?”, exploring follow-up questions, and creating tools to benchmark logic capabilities in Neuro-Symbolic systems.

Having such a benchmarking system can act as a sort of “Canary in the coal mine” to detect when novel AI models are getting close to exhibiting logical reasoning.

## Genesis
I focused on a small domain with inherent logic: creating Yoga flows based on user properties. This mimics the work a Yoga teacher does before a class and can be expressed with a rule-based system.

* Q: “Give me a yoga flow for strengthening abs, the practictioner has glaucoma.”
* Step 1: Run rules-based system that gives a list of appropriate poses |P1..Pn|.
* Step 2: Feed |P1..Pn| to LLM and let it write a human-readable description.
* A: “Stand in MOUNTAIN pose … transition to … EXTENDED MOUNTAIN pose … etc …”

Step 1 logic prevents counter-indicated poses (e.g., no inverted poses for glaucoma) and ensures the poses flow smoothly (e.g., don’t go from lying down to standing without an intermediate pose).

While naively trying to implement this kind of system I ran into two obvious questions:

**1) Where do we execute the logic used in Step 1?**
- External Logical Inference Engine connected through API.
- Use context to try to teach the LLM the rules.
- In-model through fine-tunes.
- In the foundation model.
**2) What kind of approach gives acceptable latency?**
- Conversational UX needs sub-200ms latency & 150 (spoken) to 300 (read) tpm.
- This rules out complex cloud-based pipelines & bigger contexts.

While playing around with the toy Yoga domain I realised that I just assumed “LLMs can’t do logic on their own” & rushed head-first into researching ways to integrate rule-based logic systems with LLMs. But some bigger questions loom:

**Do LLMs understand logic or just probabistically mimick logic? Are they improving at logic? At what rate?**

## Research Questions

### Do Large Language Models Understand Logic or Just Mimick Context? (Replication)

Yan & al. confirm that in-context learning of logical rules simply increases the probability that models arrive at correct answers to logical questions rather than inherently understand logic.

Yet at the same time their research shows that Chain of Thought prompting seems to improve the performance of large-scale models on logical reasoning tasks, especially when using In-Context Example-based guidance rather prompt-based guidance.

Yan & al used counterfactual prompts & prompt replacement techniques to evaluate impact on logical reasoning

I would like to replicate their research & explore some of the additional open questions I discovered in the paper:

* Can alternative pre-training strategies improve logical reasoning?
* Can fine-tuning approaches improve logical reasoning?
* How does in-model logical reasoning compare to in-context reasoning?

### Benchmark


### Literature

* Yan, Junbing, Chengyu Wang, Jun Huang, and Wei Zhang. “Do Large Language Models Understand Logic or Just Mimick Context?” arXiv, February 19, 2024. http://arxiv.org/abs/2402.12091.
* Liu, Hanmeng, Zhiyang Teng, Leyang Cui, Chaoli Zhang, Qiji Zhou, and Yue Zhang. “LogiCoT: Logical Chain-of-Thought Instruction-Tuning.” arXiv, October 28, 2023. http://arxiv.org/abs/2305.12147.

## About Me

I don’t have formal training in machine learning, but I developed a passion for software development in the ‘90s and have been programming ever since.

I worked on shopping systems before the dot-com bubble, then joined a bioinformatics research group in Belgium where I first encountered machine learning. Later, I was part of a “Semantic Web” research group in Germany.

I did iOS development after the iPhone launched but got burned out on software-as-a-job. Since 2020, I’ve run a small company making chalk and skincare products for climbers (chalkrebels.com).

Today, I spend 20% of my time on “hobby” software and learning projects. I’m no AI expert, but I’m eager to learn and experiment, especially in a domain I’m passionate about.

##  Prior Related Work

I have experience building chat-based tools, including a FB Messenger payment bot for a local bank and an iOS chat app for workouts, from before the current LLM wave.

I also researched Web3 (Semantic Web) approaches for a European project in 2007-2008, sparking my interest in symbolic methods.

Previously, I worked on European genome sequencing projects in bioinformatics, which introduced me to machine learning, particularly SVMs.

## Publications

* Andreas Hess, Christian Maass, Francis Dierick (2008) From Web 2.0 to the Semantic Web: A Semi- Automated Approach. CISWeb Workshop at ESWC 2008.
* Francis Dierick, Philipp Dopichaj, Uwe Fleischer, Andreas Hess, Andre Skusa and Christian Maass (2008) Playful Validation of Automatically Extracted Data. Workshop "Nutzerinteraktion im Social Semantic Web" at "Mensch und Computer" conference.
* Sterck, L., Rombauts, S., Fawcett, J., Lin, Y.-C., Robbens, S., Wuyts, J., Dierick, F., Rouze, P., Van de Peer, Y. (2007) Eukaryotic Genome Annotation. IUAP- BioMAGNET Kick-off meeting 2007
* Rombauts, S., Sterck, L., Dierick, F., Robbens, S., Wuyts, J., Schiex, T., Rouze, P., Van de Peer, Y. (2006) Eukaryote Genome annotation at the Plant Systems Group