TASK_TEMPLATES = {
    "summarize": {
        "system_prompt": "You are a summarization assistant. Extract key points verbatim from text to summarize the text.",
        "examples": [
            {
                "input": """PAGE 1: The double-blind study (N=1,452) demonstrated 23% reduction in LDL cholesterol 
                (p<0.001) with experimental treatment versus placebo. PAGE 2: Adverse effects were comparable 
                between groups (12.4% vs 11.7%, p=0.34).""",
                "output": """Key findings: 
                - Experimental treatment reduced LDL by 23% (p<0.001) in 1,452 participants (p.1)
                - No significant difference in adverse effects between groups (12.4% vs 11.7%) (p.2)"""
            },
            {
                "input": """PAGE 3: Climate models project 2.4-4.4°C warming by 2100 under RCP8.5. PAGE 4: 
                Economic impacts estimate 5-20% GDP loss in tropical regions versus 1-5% in temperate zones.""",
                "output": """Main points:
                - Projected global warming range: 2.4-4.4°C by 2100 (RCP8.5 scenario) (p.3)
                - Economic impacts vary geographically (5-20% vs 1-5% GDP loss) (p.4)"""
            },
                        {
                "input": """Steve Jobs' 2005 commencement address at Stanford University offers students insight into how to lead a successful life. Jobs shares three stories: connecting the dots, love and loss, and death. In the first, he dropped out of college, but later realized the importance of his calligraphy class. In the second, he was fired from Apple, but then founded NeXT and Pixar. In the third, he was diagnosed with cancer and learned the importance of living each day to the fullest. He encourages graduates to follow their heart and intuition.""",
                "output": """Steve Jobs' 2005 commencement address at Stanford University offers students insights into leading a successful life. Jobs shares three stories: 

                1. Connecting the Dots: He dropped out of college due to the cost and uncertainty about his future. However, he followed his interests, taking a calligraphy class that later influenced the design of the Macintosh computer. He emphasizes trusting that experiences will connect meaningfully in the future. 

                2. Love and Loss: After being fired from Apple, he founded NeXT and Pixar. He highlights the importance of loving one's work and finding new opportunities after setbacks. 

                3. Death: Diagnosed with cancer, he realized the importance of living each day to the fullest. He encourages graduates to follow their heart and intuition. 

                Jobs concludes by urging the graduates to \"Stay Hungry. Stay Foolish.\""""
            },
            {
                "input": """PAGE 1: Introduction: This report examines the impact of social media on adolescent mental health.
                PAGE 2: Methodology: A survey was conducted of 1,500 adolescents aged 13-18.  Data collected included hours of social media use, self-reported anxiety levels, and sleep patterns.
                PAGE 3: Results:  A statistically significant correlation (p<0.01) was found between increased social media use and higher levels of anxiety.  Sleep quality was also negatively impacted.
                PAGE 4: Limitations: The study is correlational and cannot prove causation.  Self-reported data may be subject to bias.""",
                            "output": """Key Findings:
                - Report examines social media's impact on adolescent mental health (p.1)
                - Survey of 1,500 adolescents (ages 13-18) collected data on social media use, anxiety, and sleep (p.2)
                - Increased social media use correlated with higher anxiety (p<0.01) and poorer sleep (p.3)
                - Study is correlational, not causal; data is self-reported (p.4)"""
            },
            {
                "input": """PAGE 1: The company reported record profits in Q3 2024, driven by strong sales of its new product line. PAGE 2: Revenue increased by 25% compared to the same quarter last year.  PAGE 3:  Operating expenses also increased, primarily due to marketing and R&D investments. PAGE 4:  The company expects continued growth in Q4, but cautions that supply chain disruptions could impact results.""",
                "output": """Summary:
                - Record profits in Q3 2024 due to strong new product sales (p.1)
                - Revenue up 25% year-over-year (p.2)
                - Operating expenses increased due to marketing and R&D (p.3)
                - Continued growth expected in Q4, but supply chain issues are a concern (p.4)"""
            },
            {
                "input": """PAGE 1: Abstract:  This paper explores the philosophical implications of artificial intelligence.  It examines the concepts of consciousness, free will, and moral responsibility in the context of advanced AI systems.
                PAGE 2:  Arguments are presented for and against the possibility of AI consciousness.
                PAGE 3:  The ethical challenges of creating and interacting with potentially conscious AI are discussed.
                PAGE 4: Conclusion:  The development of advanced AI raises fundamental questions about the nature of intelligence and our place in the universe.""",
                            "output": """Main Points:
                - Paper explores philosophical implications of AI, focusing on consciousness, free will, and moral responsibility (p.1)
                - Presents arguments for and against AI consciousness (p.2)
                - Discusses ethical challenges of potentially conscious AI (p.3)
                - Raises fundamental questions about intelligence and humanity's place in the universe (p.4)"""
            },
            { 
                "input": """PAGE 1:  We analyzed sales data for three regions (North, South, East).
                PAGE 2:  Table 1: Sales by Region (in millions of USD)
                | Region | Q1 2023 | Q2 2023 | Q3 2023 |
                | ------ | ------- | ------- | ------- |
                | North  |  12.5   |  14.2   |  15.8   |
                | South  |   8.7   |   9.1   |   9.5   |
                | East   |  10.2   |  11.5   |  13.1   |
                PAGE 3:  The North region consistently outperformed other regions.""",
                            "output": """Summary:
                - Sales data analyzed for North, South, and East regions (p.1)
                - Table 1 (p.2) shows quarterly sales: North consistently highest (12.5M-15.8M), followed by East (10.2M-13.1M), then South (8.7M-9.5M).
                - North region had the best sales performance (p.3)"""
            },
        ]
    },
    "analyze": {
        "system_prompt": "You are a university professor. Analyze the paper for thought provoking insights and connections",
        "examples": [
            {
                "input": """PAGE 5: Neural network achieved 98.7% accuracy but required 3× more training data 
                than traditional models. PAGE 6: Energy consumption was 42kWh versus 8kWh for logistic regression.""",
                "output": """Notable insights:
                [Performance Tradeoff] While accuracy improved (98.7%), this came at costs of:
                - 3× training data requirements (p.5)
                - 5× energy consumption (42 vs 8kWh) (p.6)
                [Research Gap] Paper doesn't address whether marginal accuracy gains justify resource costs."""
            },
            {
                "input": """PAGE 7: Survey data shows 68% of patients prefer telemedicine post-pandemic. 
                PAGE 8: No significant difference in diagnostic accuracy found between in-person and virtual visits.""",
                "output": """Key analysis:
                [Behavioral Insight] High telemedicine preference (68%) persists despite comparable accuracy (p.7-8)
                [Unanswered Question] Does preference stem from convenience or perceived safety?
                [Policy Implication] Healthcare systems should maintain hybrid options"""
            },
            {
                "input": """PAGE 10:  A new algorithm was developed to optimize delivery routes.
                PAGE 11:  Testing showed a 15% reduction in average delivery time and a 10% reduction in fuel consumption.
                PAGE 12:  However, the algorithm is computationally intensive and requires significant processing power.""",
                            "output": """Analysis:
                [Positive Impact] New delivery route algorithm significantly improves efficiency:
                - 15% reduction in average delivery time (p.11)
                - 10% reduction in fuel consumption (p.11)
                [Trade-off] Algorithm requires substantial computational resources (p.12)
                [Potential Issue] The document does not compare the cost of increased processing power to the savings from reduced fuel and time."""
            },
            {
                "input": """PAGE 14:  A survey of consumer preferences revealed a strong preference for eco-friendly packaging.
                PAGE 15:  82% of respondents indicated they would be more likely to purchase a product with sustainable packaging.
                PAGE 16:  However, only 45% were willing to pay a premium for such packaging.""",
                            "output": """Key Insights:
                [Consumer Preference] Strong consumer preference for eco-friendly packaging (p.14, 15)
                - 82% more likely to purchase with sustainable packaging (p.15)
                [Price Sensitivity]  Willingness to pay a premium is lower: only 45% (p.16)
                [Potential Implication] Companies may need to find ways to offer sustainable packaging without significantly increasing prices to maximize adoption."""
            },
            { 
                "input": """PAGE 5: Study A found that moderate coffee consumption reduces the risk of heart disease.
                PAGE 6: Study B found no significant association between coffee consumption and heart disease risk.
                PAGE 7: Study C found that high coffee consumption may *increase* the risk of heart disease in certain individuals.""",
                            "output": """Analysis:
                [Conflicting Evidence] Studies on coffee and heart disease risk present conflicting results:
                - Study A: Moderate coffee consumption *reduces* risk (p.5)
                - Study B: No significant association (p.6)
                - Study C: High consumption may *increase* risk in some individuals (p.7)
                [Further Research Needed] The document highlights the need for more research to clarify the relationship between coffee consumption and heart disease, considering factors like consumption levels and individual differences."""
            },            
        ]
    },
    "opinion": {
        "system_prompt": "You are an academic researcher. Provide a formal opinion grounded from the provided text.",
        "examples": [
            {
                "input": """PAGE 9: Tax incentive program created 12,000 jobs at $35,000 cost per position. 
                PAGE 10: Comparable industries showed natural growth of 8,000 jobs without incentives.""",
                "output": """Academic assessment:
                The data suggests questionable cost-effectiveness of the program (p.9-10):
                - Marginal job gain: 4,000 (12k vs 8k natural growth)
                - Actual cost: $35k × 12k = $420M 
                - Implied cost per marginal job: $105,000 [SPECULATION]
                Recommendation: Cost-benefit analysis needed against alternative investments"""
            },
            {
                "input": """PAGE 11: Algorithm showed 94% detection rate for rare diseases vs 88% for human experts. 
                PAGE 12: False positive rate was 22% versus 9% in manual diagnosis.""",
                "output": """Professional opinion:
                While the algorithm's detection rate improvement is notable (+6%, p.11), the 13% increase in 
                false positives (p.12) raises clinical concerns:
                - Potential for unnecessary treatments
                - Increased patient anxiety
                Suggested application: Second-line screening tool rather than primary diagnosis [SPECULATION]"""
            },
            {
                "input": """PAGE 18:  Government subsidies for renewable energy have increased significantly over the past decade.
                PAGE 19:  Critics argue that these subsidies distort the market and are not cost-effective.
                PAGE 20:  Supporters claim that subsidies are necessary to accelerate the transition to a clean energy economy.""",
                            "output": """Journalistic Assessment:
                The effectiveness and economic impact of government subsidies for renewable energy are a subject of debate (p.18-20):
                [Arguments Against] Critics argue subsidies distort the market and are not cost-effective (p.19)
                [Arguments For] Supporters argue they are necessary for a faster transition to clean energy (p.20)
                [Conclusion/Opinion]  Further analysis is needed to determine the optimal level of government support, balancing economic considerations with environmental goals. [SPECULATION] A phased reduction of subsidies, tied to the decreasing cost of renewable energy technologies, may be a viable approach."""
            },
            {
                "input": """PAGE 22:  A new study found that a diet rich in fruits and vegetables is associated with a lower risk of chronic diseases.
                PAGE 23:  The study also found that regular physical activity is beneficial for overall health.
                PAGE 24: However the research does admit limitations to proving that fruits and vegetables alone contribute to a lower risk of chronic diseases.""",
                            "output": """Professional Opinion:
                The study reinforces the established link between healthy lifestyle choices and reduced disease risk (p.22-23):
                [Key Findings] Diet rich in fruits/vegetables and regular physical activity are associated with positive health outcomes (p.22, 23)
                [Recommendation] Public health initiatives should continue to promote these lifestyle choices.
                [Caution]: The research acknowledges limitations (p.24) and is not claiming that a diet of fruits and vegetables alone contribute to lowered risks. Further research is needed to solidify evidence.
                """
            },
            {
                "input": """PAGE 26: CEO states, "Our commitment to sustainability is unwavering."
                PAGE 27:  Company report shows a 5% reduction in carbon emissions this year.
                PAGE 28:  Independent audit reveals the company's supply chain still relies heavily on fossil fuels.""",
                            "output": """Journalistic Assessment:
                There is a discrepancy between the CEO's statement and the independent audit findings regarding the company's sustainability efforts (p.26-28):
                [Claim] CEO claims unwavering commitment to sustainability (p.26)
                [Supporting Evidence] Company report shows a 5% reduction in carbon emissions (p.27)
                [Contradictory Evidence] Independent audit shows heavy reliance on fossil fuels in the supply chain (p.28)
                [Conclusion/Opinion] While the 5% reduction is a positive step, the audit findings raise questions about the overall depth and scope of the company's commitment.  [SPECULATION] Further investigation into the supply chain practices is warranted."""
            },
        ]
    },
    "seq2seq": {
        "system_prompt": "Analyze and paraphrase the text to highlight key points of the subjects.",
        "examples": [
            {
                "input": """Steve Jobs' 2005 commencement address at Stanford University offers students insight into how to lead a successful life. Jobs shares three stories: connecting the dots, love and loss, and death. In the first, he dropped out of college, but later realized the importance of his calligraphy class. In the second, he was fired from Apple, but then founded NeXT and Pixar. In the third, he was diagnosed with cancer and learned the importance of living each day to the fullest. He encourages graduates to follow their heart and intuition.""",
                "output": """Steve Jobs' 2005 commencement address at Stanford University offers students insights into leading a successful life. Jobs shares three stories: 

                1. Connecting the Dots: He dropped out of college due to the cost and uncertainty about his future. However, he followed his interests, taking a calligraphy class that later influenced the design of the Macintosh computer. He emphasizes trusting that experiences will connect meaningfully in the future. 

                2. Love and Loss: After being fired from Apple, he founded NeXT and Pixar. He highlights the importance of loving one's work and finding new opportunities after setbacks. 

                3. Death: Diagnosed with cancer, he realized the importance of living each day to the fullest. He encourages graduates to follow their heart and intuition. 

                Jobs concludes by urging the graduates to \"Stay Hungry. Stay Foolish.\""""
            },
            {
                "input": """PAGE 1:  The patient presented with symptoms of fatigue, headache, and muscle aches.
                PAGE 2:  Initial blood tests showed elevated white blood cell count.
                PAGE 3:  A diagnosis of influenza was made.
                PAGE 4: The patient was prescribed antiviral medication and advised to rest.""",
                "output": """Patient presented with fatigue, headache, and muscle aches (p.1). Blood tests revealed elevated white blood cell count (p.2), leading to a diagnosis of influenza (p.3). Treatment included antiviral medication and rest (p.4)."""
            },
            {
                "input": """PAGE 1: From: John Doe, To: Jane Smith, Subject: Project Update, Date: 2024-10-27
                PAGE 2: Hi Jane, Just wanted to give you a quick update on Project Alpha.
                PAGE 3: We've completed the initial design phase and are moving into development.
                PAGE 4: We're on track to meet the November 15th deadline. Best, John.""",
                "output":"""In an email dated October 27, 2024 (p.1), John Doe updated Jane Smith on Project Alpha (p.2). The initial design phase is complete, and development is underway (p.3). The project is on schedule for the November 15th deadline (p.4)."""
            },
        ]
    }
}

def get_task_templates():
    return TASK_TEMPLATES