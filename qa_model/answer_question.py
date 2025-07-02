from transformers import pipeline

# Load QA pipeline once
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def get_answer(question, top_chunks):
    """
    Uses a transformer QA model to extract the best answer from the combined context.
    """
    context = " ".join(top_chunks)

    result = qa_pipeline({
        "question": question,
        "context": context
    })

    answer = result.get("answer", "")
    score = result.get("score", 0)

    if score < 0.3 or answer.strip() == "":
        return "🤔 Sorry, I couldn’t find a confident answer from the given Wikipedia pages."

    return f"**Answer:** {answer}\n\n_(Confidence: {round(score * 100, 2)}%)_"