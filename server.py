"""
Flask server for the Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


def run_emotion_detection():
    """
    Run the Flask Emotion Detection application.
    """
    app.run(host="0.0.0.0", port=5000)


@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the submitted text and return its emotions.
    """
    text_to_detect = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_detect)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render the application's home page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    run_emotion_detection()
    