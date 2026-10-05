import os
import textwrap

import streamlit as st
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

try:
    from google import genai
except ImportError:
    genai = None


# ============================================================
# HTML HELPER
# ============================================================

def html(content):
    """
    Render HTML directly instead of passing it through
    Streamlit Markdown.
    """
    st.html(textwrap.dedent(content))


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
    color: #17365d;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.result {
    padding: 20px;
    border-radius: 15px;
    background-color: #eef5ff;
    margin-top: 15px;
    margin-bottom: 20px;
}

.ai-card {
    padding: 25px;
    border-radius: 18px;
    background: linear-gradient(135deg, #eef5ff, #f8faff);
    border: 1px solid #d7e6ff;
    margin-top: 15px;
    margin-bottom: 20px;
}

.hero-card {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #eef5ff, #ffffff);
    border: 1px solid #dce9f9;
    margin-bottom: 25px;
}

.step {
    padding: 14px;
    margin: 10px 0;
    border-radius: 12px;
    background-color: #f7f9fc;
}

.step-number {
    font-size: 20px;
    font-weight: 700;
    color: #2457a6;
}

.card h3 {
    color: #17365d;
}

.card h2 {
    color: #2457a6;
    margin-bottom: 0;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

html("""
<div class="title">
    🎓 AI Career Guidance System
</div>

<div class="subtitle">
    Discover the career path that best matches your skills, interests and goals.
</div>
""")


# ============================================================
# CAREER DATABASE
# ============================================================

career_data = {

    "Software Developer": {
        "skills": [
            "Python",
            "Java",
            "C++",
            "Programming",
            "Problem Solving"
        ],
        "interests": [
            "Coding",
            "Technology",
            "Software",
            "Web Development"
        ],
        "learn": [
            "Python/Java",
            "Data Structures",
            "Algorithms",
            "Git",
            "Web Development"
        ]
    },

    "Data Scientist": {
        "skills": [
            "Python",
            "Statistics",
            "Machine Learning",
            "SQL",
            "Data Analysis"
        ],
        "interests": [
            "Data",
            "AI",
            "Statistics",
            "Research",
            "Analytics"
        ],
        "learn": [
            "Python",
            "Statistics",
            "Pandas",
            "Machine Learning",
            "SQL"
        ]
    },

    "AI / ML Engineer": {
        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch"
        ],
        "interests": [
            "Artificial Intelligence",
            "Machine Learning",
            "Robotics",
            "Research"
        ],
        "learn": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "Computer Vision"
        ]
    },

    "Web Developer": {
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Frontend"
        ],
        "interests": [
            "Web Development",
            "Design",
            "Frontend",
            "Technology"
        ],
        "learn": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "APIs"
        ]
    },

    "Cybersecurity Analyst": {
        "skills": [
            "Networking",
            "Linux",
            "Python",
            "Cybersecurity",
            "Ethical Hacking"
        ],
        "interests": [
            "Security",
            "Networking",
            "Cybersecurity",
            "Ethical Hacking"
        ],
        "learn": [
            "Computer Networks",
            "Linux",
            "Python",
            "Cybersecurity",
            "Ethical Hacking"
        ]
    },

    "Cloud Engineer": {
        "skills": [
            "AWS",
            "Azure",
            "Linux",
            "Networking",
            "Docker"
        ],
        "interests": [
            "Cloud",
            "Servers",
            "Networking",
            "DevOps",
            "Technology"
        ],
        "learn": [
            "Linux",
            "AWS/Azure",
            "Docker",
            "Kubernetes",
            "Networking"
        ]
    },

    "UI/UX Designer": {
        "skills": [
            "Figma",
            "UI Design",
            "UX Design",
            "Creativity",
            "Prototyping"
        ],
        "interests": [
            "Design",
            "Creativity",
            "UI",
            "UX",
            "Art"
        ],
        "learn": [
            "Figma",
            "UI Design",
            "UX Research",
            "Prototyping",
            "Design Systems"
        ]
    }
}


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("👤 Student Profile")

    name = st.text_input(
        "Your Name"
    )

    education = st.selectbox(
        "Education",
        [
            "B.Tech / Engineering",
            "B.Sc",
            "BCA",
            "MCA",
            "MBA",
            "Intermediate",
            "Other"
        ]
    )

    branch = st.selectbox(
        "Branch / Stream",
        [
            "Computer Science",
            "Information Technology",
            "Electronics",
            "Electrical",
            "Mechanical",
            "Civil",
            "Other"
        ]
    )

    experience = st.selectbox(
        "Experience Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    skills_input = st.text_area(
        "Your Skills",
        placeholder="Example: Python, Java, SQL, HTML, Machine Learning"
    )

    interests_input = st.text_area(
        "Your Interests",
        placeholder="Example: AI, coding, web development, data"
    )

    preferred_work = st.selectbox(
        "Preferred Work Type",
        [
            "Software Development",
            "Data & Analytics",
            "Artificial Intelligence",
            "Web Development",
            "Cybersecurity",
            "Cloud & DevOps",
            "Design",
            "Not Sure"
        ]
    )

    st.markdown("---")

    generate = st.button(
        "🚀 Get Career Guidance",
        use_container_width=True
    )


# ============================================================
# CAREER MATCHING
# ============================================================

def calculate_matches(skills, interests):

    skills = [
        x.strip().lower()
        for x in skills.split(",")
        if x.strip()
    ]

    interests = [
        x.strip().lower()
        for x in interests.split(",")
        if x.strip()
    ]

    results = []

    for career, data in career_data.items():

        career_skills = [
            x.lower()
            for x in data["skills"]
        ]

        career_interests = [
            x.lower()
            for x in data["interests"]
        ]

        skill_matches = 0
        interest_matches = 0

        for skill in skills:

            if any(
                skill in cs or cs in skill
                for cs in career_skills
            ):
                skill_matches += 1

        for interest in interests:

            if any(
                interest in ci or ci in interest
                for ci in career_interests
            ):
                interest_matches += 1

        skill_score = (
            skill_matches / len(career_skills) * 60
            if career_skills
            else 0
        )

        interest_score = (
            interest_matches / len(career_interests) * 40
            if career_interests
            else 0
        )

        score = min(
            100,
            skill_score + interest_score
        )

        results.append({
            "Career": career,
            "Match Score": round(score, 1),
            "Matched Skills": skill_matches,
            "Matched Interests": interest_matches
        })

    results.sort(
        key=lambda x: x["Match Score"],
        reverse=True
    )

    return results


# ============================================================
# GEMINI AI
# ============================================================

def generate_ai_guidance(
    name,
    education,
    branch,
    experience,
    skills,
    interests,
    preferred_work,
    careers
):

    api_key = os.getenv("GEMINI_API_KEY")

    if genai is None:
        return {
            "success": False,
            "message": (
                "Google GenAI is not installed. "
                "Run: python -m pip install -U google-genai"
            )
        }

    if not api_key:
        return {
            "success": False,
            "message": (
                "GEMINI_API_KEY was not found. "
                "Check your .env file."
            )
        }

    try:

        client = genai.Client(
            api_key=api_key
        )

        career_text = ", ".join(
            [
                f"{x['Career']} ({x['Match Score']}%)"
                for x in careers[:5]
            ]
        )

        prompt = f"""
You are an AI Career Guidance expert helping a college student.

Student Information:

Name: {name}
Education: {education}
Branch: {branch}
Experience: {experience}
Skills: {skills}
Interests: {interests}
Preferred Work Type: {preferred_work}

Top career matches:

{career_text}

Give practical career guidance.

Include:

1. Best career recommendation
2. Why it matches the student
3. Skills to learn
4. Project ideas
5. Internship preparation
6. A 6-month learning roadmap
7. Suitable job roles

Use simple language.
Use headings and bullet points.
Keep the response concise.
"""

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt,
            generation_config={
                "thinking_level": "low"
            }
        )

        answer = interaction.output_text

        if answer:
            return {
                "success": True,
                "message": answer
            }

        return {
            "success": False,
            "message": "Gemini returned an empty response."
        }

    except Exception as e:

        return {
            "success": False,
            "message": f"Gemini API error: {str(e)}"
        }
        if response and response.text:

            return {
                "success": True,
                "message": response.text
            }

        return {
            "success": False,
            "message": "Gemini returned an empty response."
        }

    except Exception as e:

        return {
            "success": False,
            "message": f"Gemini API error: {str(e)}"
        }


# ============================================================
# PROJECT IDEAS
# ============================================================

project_ideas = {

    "Software Developer": [
        "Student Management System",
        "Online Payment System",
        "Task Management Application"
    ],

    "Data Scientist": [
        "Student Performance Prediction",
        "Sales Data Analysis",
        "Customer Churn Prediction"
    ],

    "AI / ML Engineer": [
        "AI Career Guidance System",
        "Fake News Detection",
        "AI Chatbot"
    ],

    "Web Developer": [
        "Portfolio Website",
        "E-Commerce Website",
        "Social Media Dashboard"
    ],

    "Cybersecurity Analyst": [
        "Phishing Website Detector",
        "Password Strength Analyzer",
        "Network Security Monitor"
    ],

    "Cloud Engineer": [
        "Cloud File Storage System",
        "Dockerized Web Application",
        "Cloud Monitoring Dashboard"
    ],

    "UI/UX Designer": [
        "College App UI",
        "Travel App Design",
        "Healthcare App Prototype"
    ]
}


# ============================================================
# RESULTS
# ============================================================

if generate:

    if not name.strip():

        st.warning(
            "⚠️ Please enter your name."
        )

    elif not skills_input.strip():

        st.warning(
            "⚠️ Please enter at least a few skills."
        )

    elif not interests_input.strip():

        st.warning(
            "⚠️ Please enter your interests."
        )

    else:

        results = calculate_matches(
            skills_input,
            interests_input
        )

        st.success(
            f"Career analysis completed for {name}! 🎯"
        )

        # ----------------------------------------------------
        # PROFILE SUMMARY
        # ----------------------------------------------------

        st.subheader("👤 Your Profile")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Education",
                education
            )

        with col2:
            st.metric(
                "Branch",
                branch
            )

        with col3:
            st.metric(
                "Experience",
                experience
            )

        with col4:
            st.metric(
                "Career Options",
                len(results)
            )

        # ----------------------------------------------------
        # TOP CAREERS
        # ----------------------------------------------------

        st.subheader("🏆 Your Top Career Matches")

        career_cols = st.columns(3)

        for index, career in enumerate(results[:3]):

            medal = (
                "🥇"
                if index == 0
                else "🥈"
                if index == 1
                else "🥉"
            )

            with career_cols[index]:

                html(f"""
<div class="card">
    <h3>{medal} {career['Career']}</h3>
    <h2>{career['Match Score']}%</h2>
    <p>Career Match Score</p>
</div>
""")


        # ----------------------------------------------------
        # MATCH ANALYSIS
        # ----------------------------------------------------

        st.subheader("📊 Career Match Analysis")

        df = pd.DataFrame(results)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        # ----------------------------------------------------
        # BEST CAREER
        # ----------------------------------------------------

        best_career = results[0]["Career"]

        html(f"""
<div class="result">
    <h2>🎯 Recommended Career: {best_career}</h2>

    <p>
        Based on your skills and interests,
        <b>{best_career}</b> is currently your
        strongest career match.
    </p>
</div>
""")

        # ----------------------------------------------------
        # SKILLS
        # ----------------------------------------------------

        st.subheader("📚 Skills You Should Learn")

        recommended_skills = career_data[
            best_career
        ]["learn"]

        skill_cols = st.columns(3)

        for i, skill in enumerate(
            recommended_skills
        ):

            with skill_cols[i % 3]:

                st.info(
                    f"📌 {skill}"
                )

        # ----------------------------------------------------
        # ROADMAP
        # ----------------------------------------------------

        st.subheader("🛣️ Suggested Learning Roadmap")

        roadmap = [

            (
                "Month 1",
                "Strengthen programming fundamentals"
            ),

            (
                "Month 2",
                "Learn core technologies required for the career"
            ),

            (
                "Month 3",
                "Practice problem solving and small projects"
            ),

            (
                "Month 4",
                "Build one major portfolio project"
            ),

            (
                "Month 5",
                "Prepare resume and apply for internships"
            ),

            (
                "Month 6",
                "Practice interviews and build your portfolio"
            )
        ]

        for month, task in roadmap:

            st.markdown(
                f"**{month} →** {task}"
            )

        # ----------------------------------------------------
        # PROJECT IDEAS
        # ----------------------------------------------------

        st.subheader("💡 Project Ideas")

        for project in project_ideas[best_career]:

            st.write(
                f"🔹 {project}"
            )

        # ----------------------------------------------------
        # AI ADVISOR
        # ----------------------------------------------------

        st.subheader("🤖 AI Career Advisor")

        html("""
<div class="ai-card">
    <h3>✨ Personalized AI Guidance</h3>

    <p>
        Gemini analyzes your profile and provides
        personalized career recommendations,
        skills, projects, internships and a
        6-month roadmap.
    </p>
</div>
""")

        with st.spinner(
            "🤖 Gemini is analyzing your career profile..."
        ):

            ai_result = generate_ai_guidance(
                name,
                education,
                branch,
                experience,
                skills_input,
                interests_input,
                preferred_work,
                results
            )

        if ai_result["success"]:

            st.success(
                "✨ Personalized AI guidance generated successfully!"
            )

            st.markdown(
                ai_result["message"]
            )

        else:

            st.error(
                "❌ AI Advisor could not generate guidance."
            )

            st.warning(
                ai_result["message"]
            )

            st.info(
                "💡 Your normal career matching system is still working."
            )


# ============================================================
# HOME PAGE
# ============================================================

else:

    html("""
<div class="hero-card">

    <h2>🌟 How It Works</h2>

    <div class="step">
        <span class="step-number">
            1️⃣ Enter your profile
        </span>
        <br>
        Provide your education, skills and interests.
    </div>

    <div class="step">
        <span class="step-number">
            2️⃣ AI analyzes your profile
        </span>
        <br>
        The system compares your profile with different
        career paths.
    </div>

    <div class="step">
        <span class="step-number">
            3️⃣ Get career recommendations
        </span>
        <br>
        You receive career match scores and recommended
        career options.
    </div>

    <div class="step">
        <span class="step-number">
            4️⃣ Get personalized AI guidance
        </span>
        <br>
        Gemini provides career advice, skills,
        projects, internships and a learning roadmap.
    </div>

    <div class="step">
        <span class="step-number">
            5️⃣ Follow your roadmap
        </span>
        <br>
        Build your skills and prepare for your future career.
    </div>

</div>
""")

    st.info(
        "💡 Tip: Enter skills and interests separated by commas "
        "for better results."
    )