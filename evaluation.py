from scoring import score_output

def run_evaluation(name):
    # Placeholder for real LLM calls
    sample_output = "This is a sample model output."
    score = score_output(sample_output)
    print(f"Evaluation for '{name}': score={score}")