# Prompt Design Choices

* Model: gemini-2.5-flash
* Temperature: 0.2 for deterministic outputs during evaluation.
* Output Schema: Enforced via sentiment_schema.json, requiring:
* label ∈ {Positive, Negative, Neutral}
* confidence (0–1, 2 decimals)
* explanation (1–3 sentences)
* evident_phrases (list of sentiment-bearing phrases)
* Implementation: LangChain’s with_structured_output ensures consistent JSON.
* Streamlit app: Uses local JSON caching for cost control.

# Failure Cases & Mitigations

### **Neutral misclassifications**: 
Reviews mixing praise and critique (e.g., “Worth watching for the spectacle alone, but…”) often mislabeled as Positive.

**Mitigation**: Left as is for now, could be improved by adding few-shot neutral examples which emphasize “overall sentiment” in prompt.

### **Confidence calibration**: 
Confidence values tended to cluster high (0.95–0.98).

**Mitigation**: Left as-is for transparency; could be improved with a secondary calibration step.

### **Verbose explanations**: 
Early versions exceeded 3 sentences.

**Mitigation**: Prompt explicitly constrained to 1–3 sentences.

### Rate limiting issues: 
The Gemini free-tier API enforces a strict quota.

**Mitigation**: Added time.sleep() between batch calls in batch_eval.ipynb to avoid hitting the per-minute rate limit.

# Mini Metrics
| Metric         | Value      |
| -------------- | ---------- |
| Accuracy       | **90.57%** |
| Positive count | 20         |
| Negative count | 20         |
| Neutral count  | 13         |

# Notes

* The evaluation was run in batch_eval.ipynb over 60 IMDB-style reviews out of which few 7 failed because of rate-limit restrictions on free tier of gemini api.
* Outputs strictly follow the schema in sentiment_schema.json.
