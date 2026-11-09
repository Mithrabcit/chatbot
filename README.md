#  Bill Rescue – AI-Powered Electricity Bill Analysis Assistant

**Understand your electricity bills. Detect unusual patterns. Predict future expenses.**

##  Project Overview

Bill Rescue is an AI-powered electricity bill analysis and assistance platform designed to help consumers understand, monitor, and manage their electricity expenses.

Electricity bills often contain technical terms, multiple charge components, tariff calculations, and consumption details that may be difficult for consumers to understand. Bill Rescue simplifies this process by combining Artificial Intelligence (AI), Machine Learning (ML), and Retrieval-Augmented Generation (RAG).

Users can upload their electricity bills, compare consumption across billing periods, identify unusual usage patterns, estimate future bills, and ask questions about electricity tariffs through an AI-powered chatbot.

The platform also introduces intelligent features such as appliance-wise cost estimation, prediction accuracy tracking, explainable anomaly detection, multilingual voice interaction, and a what-if bill simulator.

## Project Objectives

- Simplify electricity bill analysis and understanding.
- Identify unusual electricity consumption patterns.
- Predict future electricity usage and estimated expenses.
- Provide understandable explanations of bill changes.
- Help consumers explore electricity costs using interactive simulations.
- Make electricity-related information accessible through text and voice.

 Key Functionalities

##  📄 Electricity Bill Upload and Data Extraction

Users can upload their electricity bills in PDF format.

The system extracts important information, including:

- Consumer category
- Previous meter reading
- Current meter reading
- Units consumed
- Billing period
- Fixed charges
- Energy charges
- Additional charges
- Total bill amount
- Due date

The extracted information is converted into structured data for further analysis. The system can also be extended with OCR to process scanned bill images.

##  📊 Current and Previous Bill Comparison

Bill Rescue compares the current electricity bill with previous billing records.

It analyses:

- Changes in electricity consumption.
- Differences in total bill amounts.
- Changes in individual charge components.
- Consumption variations across billing periods.

The results are displayed using charts and summaries, helping users understand why their electricity expenses may have increased or decreased.

##  AI-Based Electricity Bill Assistant

The platform includes a Gemini-powered chatbot that answers questions related to electricity bills.

Users can ask questions such as:

- Why has my electricity bill increased?
- What does energy consumption mean?
- How are electricity charges calculated?
- What should I check if my bill appears unusually high?

The chatbot provides understandable explanations using the available bill information and relevant electricity tariff documents.

## RAG-Based Tariff Information Retrieval

Bill Rescue uses Retrieval-Augmented Generation (RAG) to provide answers based on electricity tariff documents.

The process involves:

1. Extracting text from official tariff documents.
2. Dividing the extracted content into smaller sections.
3. Generating embeddings for the text.
4. Storing the embeddings in ChromaDB.
5. Retrieving relevant information when a user asks a question.
6. Sending the retrieved context to Gemini to generate an understandable response.

This helps the chatbot provide document-grounded answers instead of relying only on general AI knowledge.



##  How Bill Rescue Works

1. The user opens the Bill Rescue application.
2. The user uploads an electricity bill or interacts with the chatbot.
3. The backend extracts and validates available bill information.
4. The structured bill data is used for comparison and analysis.
5. Machine learning models analyse consumption patterns and estimate future usage.
6. The anomaly detection module identifies unusual consumption patterns.
7. The RAG pipeline retrieves relevant tariff information when needed.
8. The Gemini-powered assistant generates understandable explanations.
9. Additional modules provide appliance cost estimates, prediction tracking, voice interaction, and what-if simulations.
10. Results are presented through an interactive dashboard.


**Bill Rescue – Making Electricity Bills Easier to Understand.** ⚡
