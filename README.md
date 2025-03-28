# UniQuestAI

UniQuestAI is an **AI-powered multi-agent system** designed to help students efficiently discover and explore **university admissions** worldwide. By leveraging **agentic AI workflows**, UniQuestAI automates the tedious process of searching, extracting, and compiling university admission-related information, allowing students to focus on **preparing applications and gathering necessary documents**.

## 🚀 Features
- **Search Top Universities** based on discipline, education level, and location
- **Extract Admission & Program Details** automatically
- **Compile Structured University Data** into an Excel sheet
- **Multi-Agent Collaboration** for efficient information retrieval
- **User-Friendly Streamlit Interface** for seamless interaction

## 📂 Project Structure
```
uniquest-ai/                    # Main project folder
│── frontend/                    # Frontend directory
│   ├── app.py                   # Streamlit application
│
│── backend/                     # Backend directory
│   ├── main.py                   # FastAPI backend
│   ├── utils.py                  # Utility functions
│
│   ├── agents/                   # Agents folder
│   │   ├── university_search_agent.py
│   │   ├── program_search_agent.py
│   │   ├── information_extraction_agent.py
│   │   ├── information_processing_agent.py
│   │
│   ├── workflows/                # Workflows folder
│   │   ├── uniquest_workflow.py
│
│── requirements.txt              # Dependencies
│── .env                          # Environment variables
│── LICENSE                       # License file
│── README.md                     # Project documentation
```

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)  
- **Agentic AI Framework:** [agno](https://docs.agno.com/introduction)  

## 🏗️ System Design
UniQuestAI is built as a **multi-agent collaborative system** where four specialized agents work together to automate the university search and data extraction process:
1. **University Search Agent** – Identifies top universities based on rankings and user preferences.
2. **Program Search Agent** – Searches admission and program-specific links from official university websites.
3. **Information Extraction Agent** – Extracts key admission requirements and program details such as GRE/IELTS requirements, deadlines, fees, etc.
4. **Information Processing Agent** – Organizes extracted data and formats it into an JSON format for further processing.

## 🔧 Installation & Setup
### Prerequisites
- Python 3.8+
- Pip (Python Package Installer)
- Virtual Environment (Recommended)

### Steps to Set Up
1. **Clone the Repository**
   ```sh
   git clone https://github.com/aminajavaid30/uniquest-ai.git
   cd uniquest-ai
   ```
2. **Create & Activate a Virtual Environment**
   ```sh
   conda create -n uniquest
   conda activate uniquest
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables**
   - Create a `.env` file and add required API keys and configurations.

5. **Run the Backend (FastAPI)**
   ```sh
   cd backend
   uvicorn main:app --reload
   ```
6. **Run the Frontend (Streamlit App)**
   ```sh
   cd frontend
   streamlit run app.py
   ```

## 📌 Usage
- Open the **Streamlit UI** in your browser.
- Enter your **search criteria** (Discipline, Education Level, Location, etc.).
- UniQuestAI will fetch and compile **detailed admission information**.
- Download the **Excel file** for further reference.

## 📢 Challenges & Considerations
### **Challenges Faced**
- **Scraping Restrictions** – Many ranking websites block direct scraping.
- **Correct Program Links** – Finding relevant URLs instead of scanning entire university sites.
- **Token Limitations** – Managing API usage efficiently.
- **Ensuring Data Accuracy** – Preventing hallucination by LLMs.

### **Solutions Implemented**
- Used **GoogleSearchTools** for fetching top university rankings.
- Implemented **targeted link extraction** to avoid unnecessary crawling.
- Designed **workflow-based iterative processing** to optimize API token consumption.
- Applied **ReAct and Reflection patterns** to improve data reliability.

## 🔮 Future Enhancements
- Add support for **mid-tier and lower-ranked universities**.
- Improve filtering based on **Public vs. Private universities**.
- Enhance **user personalization** with more refined search options.

## 📜 License
This project is licensed under the MIT License. See the **LICENSE** file for details.

## Contributors
- **Amina Javaid** ([@https://github.com/aminajavaid30](https://github.com/aminajavaid30/uniquest-ai))
- 
---
🎯 **UniQuestAI – Your AI-powered companion for seamless university admissions research!**

