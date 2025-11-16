import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def main():
    print("Hello from langchaintutorial!")
    information = """ LeBron Raymone James Sr. (/ləˈbrɒn/[1] lə-BRON; born December 30, 1984) is an American professional basketball player for the Los Angeles Lakers of the National Basketball Association (NBA). Nicknamed "King James", he is the NBA's all-time leading scorer and has won four NBA championships from 10 NBA Finals appearances, having made eight consecutive appearances between 2011 and 2018.[2] He also won the inaugural NBA Cup in 2023 with the Lakers and has won three Olympic gold medals as a member of the U.S. national team. James is widely considered one of the greatest basketball players of all time.[3][4]

In addition to ranking fourth in NBA career assists and sixth in NBA career steals, James holds several individual honors, including four NBA MVP awards, four Finals MVP awards, the Rookie of the Year award, three All-Star Game MVP awards, the inaugural NBA Cup MVP, and the Olympics MVP in the 2024 Summer Olympics. A record 21-time All-Star and 21-time All-NBA selection (including a record 13 First Team selections), he has also made six All-Defensive Teams. The oldest active player in the NBA, he is tied with Vince Carter for the most seasons played and holds the record for the most minutes played in league history.

Born and raised in Akron, Ohio, James gained national attention at St. Vincent–St. Mary High School and was heavily touted as a future NBA superstar for his all-around scoring, passing, athleticism and playmaking abilities.[5] A prep-to-pro, James was selected by the Cleveland Cavaliers with the first overall pick of the 2003 NBA draft. He won Rookie of the Year and quickly established himself as one of the league's premier players, leading Cleveland to its first NBA Finals appearance in 2007 and winning the scoring title in 2008. After winning back-to-back MVPs in 2009 and 2010, he left the Cavaliers and joined the Miami Heat as a free agent in 2010, a controversial move announced in the nationally televised special titled The Decision.[6]

With the Heat, James won his first two NBA championships in 2012 and 2013, earning MVP and Finals MVP honors both years. After four seasons in Miami, he returned to Cleveland in 2014, leading the Cavaliers to their first-ever championship in 2016 by overcoming a 3–1 deficit against the Golden State Warriors and ending the Cleveland sports curse. He signed with the Lakers in 2018, winning another title in 2020 and becoming the first player to win Finals MVP with three different teams. In 2023, he surpassed Kareem Abdul-Jabbar to become the NBA's all-time leading scorer, and in 2024, he and his son Bronny became the first father-son teammates in league history. In 2025, James was inducted into the Naismith Memorial Basketball Hall of Fame as a member of the 2008 U.S. Olympic team (also known as the "Redeem Team"). He and Chris Paul became the first NBA players inducted into the Hall of Fame while still active.[7]

Off the court, James has earned further wealth and fame from numerous endorsement contracts. He is the first player in NBA history to accumulate $1 billion in earnings as an active player.[8] James has been featured in books, documentaries (including winning three Sports Emmy Awards as an executive producer), and television commercials. He was among Time's 100 most influential people in the world in 2005, 2013, 2017, and 2019 — the most selections for a professional athlete. James has won 20 ESPY Awards, hosted Saturday Night Live, and starred in the sports film Space Jam: A New Legacy (2021). He has been a part-owner of Liverpool F.C. since 2011 and leads the LeBron James Family Foundation, which has opened an elementary school, housing complex, retail plaza, and medical center in Akron.[9][10] """

    
    
    summary_template = """ Given the information {information} about a person, tell me a short summary and the person's age. """
    #input_variables is just metadata, which describes the dict. its just a placeholder, it can be named
    #BEST PRACTICE is to keep EVERYTHING consistent: literal variables, Template input dict, and invoke key:value pair
    summary_prompt_template = PromptTemplate(input_variables=["info"], template=summary_template)
    #f strrings can be used, but it is better to use PromptTemplate for error handling, safer for prompt injection


    llm = ChatOpenAI(temperature=0, model="gpt-5")

    #LCEL: create a chain using 2 elements, the prompt template and the LLM
    # | is the pipe operator, it creates a runnable object -> use invoke to run it
    chain = summary_prompt_template | llm

    #
    response = chain.invoke(input = {"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
