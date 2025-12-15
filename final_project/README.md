# Quiz Analytics & Leaderboard Insights

## Project Overview
This project analyzes quiz attempts and leaderboard data to evaluate learner performance, consistency, and improvement over time. Using Python, Pandas, Matplotlib, and Seaborn, the project provides insights for instructors and learning product teams.

---

## Project Goal
- Understand learner behavior in quiz environments.  
- Identify performance trends and anomalies.  
- Provide actionable feedback to learners.  

---

## Target Audience
- Instructors and educators  
- Learning product teams  
- Data analysts interested in educational insights  

---

## Dataset
**File:** `quiz_attempts.csv`  

| Column Name | Description |
|-------------|-------------|
| `user_id` | Unique identifier for each learner |
| `quiz_id` | Identifier of the quiz attempted |
| `score` | Score obtained in the quiz (0–100) |
| `time_taken` | Time taken to complete the quiz (minutes) |
| `timestamp` | Date and time of the quiz attempt |

*Note:* Users may have multiple quiz attempts (duplicates in `user_id`).  

---

## Project Features
1. **Data Exploration**
   - View first rows with `head()`  
   - Check data types using `info()`  
   - Generate summary statistics using `describe()`  

2. **Basic Statistics**
   - Compute mean, median, mode, and standard deviation for numeric features  
   - Calculate correlation between score and time taken  

3. **Visualizations**
   - **Histogram:** Distribution of scores  
   - **Scatter Plot:** Score vs Time Taken  
   - **Boxplots (Side-by-side):** Spread of scores and time taken, highlighting outliers  
   - **Correlation Heatmap:** Numeric feature relationships  

4. **Anomaly Detection**
   - Identify sudden jumps in scores for possible cheating flags  

5. **AI-Powered Feedback (Optional)**
   - **GPT-4o-mini API:** Generate personalized feedback for each learner  
   - **Rule-Based Fallback:** Ensures feedback is always available even if API quota is exceeded  
   - Feedback highlights strengths, improvement areas, and suggestions  

---

## Technologies Used
- Python  
- Pandas (Data manipulation)  
- Matplotlib & Seaborn (Data visualization)  
- OpenAI GPT-4o-mini API (Optional AI-powered feedback)  

---

## Installation
1. Clone the repository:  
```bash
git clone https://github.com//Saudii81/Flexisaf_Internship/quiz-analytics-leaderboard.git

