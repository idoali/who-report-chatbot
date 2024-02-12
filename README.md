# WHO Report Chatbot with LangChain and Streamlit

![Chatbot]("media/chatbot.gif")

## Introduction

Imagine you want to create a chatbot, like those you see on websites that can answer questions or help you with tasks. Now, there are many ways to make a chatbot, but let's focus on one of them. Let’s focus on Streamlit.

Streamlit is like a toolbox for building websites, but it's made specifically for people who know how to program in Python. So, if you're comfortable with Python, you'll find it quite easy to use.

Here's why you might want to use Streamlit to make your chatbot:

1. **Easy to Understand**: With Streamlit, you write Python code to create your chatbot, which is probably a language you're already familiar with if you've been learning programming in school. So, it's easier to understand and work with.
2. **No Need for Web Development Skills**: Unlike some other methods of building websites, you don't need to learn a bunch of extra stuff like HTML, CSS, or JavaScript. With Streamlit, you can focus on just writing Python code to make your chatbot work.
3. **Quick to See Results**: When you're working on your chatbot with Streamlit, you can see changes you make to your code right away. It's like editing a document and seeing the changes instantly. This makes it really quick to try out different ideas and see what works best.
4. **Works Well with Machine Learning**: If you want your chatbot to be smart and understand what people are saying, you might use machine learning techniques. Streamlit plays nicely with machine learning libraries like TensorFlow or PyTorch, so you can easily add that intelligence to your chatbot.
5. **Lots of Help Available**: Since Streamlit is popular, there are plenty of tutorials, guides, and people online who can help you if you get stuck. That means you're not alone in figuring things out.

We will then combine it LangChain, which is a new framework we can use to connect LLM to various other tools. You know that ChatGPT (one of the LLM out there) is quite smart right. With LangChain, it will become even smarter.

## Files

```{}
report_chatbot
|-- Hello.py
|-- docs
		|-- chroma_db
		|-- summaries.json
		|-- world-health-statistics.pdf
|-- notebook.ipynb
|-- pages
		|-- 1_☕_Summary.py
		|-- 2_🎡_Chat.py
|-- utils.py
```

## Run

To run this container you can run these commands (make sure you have docker installed).

Build the docker image

```{}
docker build -t who-report-chatbot .
```

Run the docker container

```{}
docker run --name chatbot-container -p 8501:8501 who-report-chatbot
```

## Article

For more detail explanation, you can go to this [article](https://idoali.medium.com/building-a-report-chatbot-using-langchain-and-streamlit-7fc444487596): 

