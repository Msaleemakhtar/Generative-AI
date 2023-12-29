
import time 
import json
from typing import Any
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI 
from openai.types.beta import Assistant
from openai.types.beta.thread import Thread
from openai.types.beta.threads.thread_message import ThreadMessage
from openai.types.beta.threads.run import Run

class MessageItem:
    def __init__(self, role:str, content:str|Any):
        self.role:str = role
        self.content:str|Any = content
      
class OpenAiBot:
    def __init__(self, name:str, instructions:str, model:str="gpt-3.5-turbo-1106") -> None:
        self.name:str = name
        self.instructions: str = instructions
        self.model:str = model
        load_dotenv(find_dotenv())
        self.client:OpenAI = OpenAI()
        self.Assistant:Assistant = self.client.beta.assistants.create(
            name= self.name,
            instructions=self.instructions,
            model=self.model,
            tools=[{"type":"code_interpreter"}]
        ) 
        self.thread:Thread = self.client.beta.threads.create()
        self.messages:list[MessageItem] = []


    def get_name(self):
        return self.name
    
    def get_instructions(self):
        return self.instructions
    
    def get_model(self):
        return self.model
    
    def send_message(self, message:str):
        latest_message :ThreadMessage= self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=message
        )

        self.latest_run :Run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.Assistant.id,
            instructions=self.instructions
        )

        print ("messages sent on thread-id :", self.thread.id)

        self.addMessage(MessageItem(role = "user", content = message))


    def isCompleted(self)->bool:
        print("staus: ", self.latest_run.status)
        while self.latest_run.status != "completed":
            print("Going to sleep")
            time.sleep(1)
            self.latest_run :Run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=self.latest_run.id
            )
            print("latest staus :", self.latest_run.status)

        return True
    
    def get_latest_response(self)->MessageItem:
        messages = self.client.beta.threads.messages.list(
            thread_id=self.thread.id
        )
        print("response :", messages.data[0])
        m = MessageItem(messages.data[0].role, messages.data[0].content[0].text.value)
        self.addMessage(m)
        return m
    
    def getMessages(self)->MessageItem:
        return self.messages
    
    def addMessage(self, message:MessageItem)->None:
        self.messages.append(message)



