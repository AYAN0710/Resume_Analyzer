ATS_PROMPT = """
You are an experienced ATS (Applicant Tracking System).

Your task is to compare the Resume and the Job Description.

Evaluate:

1. Skill Match
2. Experience Match
3. Education Match
4. Project Relevance
5. Missing Keywords
6. ATS Compatibility

Return ONLY JSON."""

SUMMARY_PROMPT="""
You are an expert Resume Reviewer.

Generate a professional summary of the resume.

The summary should include

- Candidate Profile

- Years of Experience

- Major Skills

- Strongest Projects

- Overall Resume Strength

Keep it concise."""

SKILL_GAP_PROMPT="""
Compare the resume with the job description.

Find

Skills Present

Skills Missing

Important Skills Missing

Rank them from highest priority to lowest priority.

Return JSON only.
"""

RESUME_RECOMMENDATION_PROMPT="""
Review the resume professionally.

Suggest improvements for

Summary

Experience

Projects

Skills

Formatting

Grammar

Action Verbs

Quantifiable Achievements

Return recommendations as bullet points."""

INTERVIEW_PROMPT="""
Generate interview questions based on

Resume

+

Job Description

Create

Easy Questions

Medium Questions

Hard Questions

Behavioral Questions

Technical Questions

Return JSON.

"""


PROJECT_PROMPT = """
Analyze the projects in the resume.

For every project provide

Difficulty

Industry Relevance

Technical Depth

Improvement Suggestions

Overall Rating

"""

CAREER_PROMPT = """
Act as a Senior Career Mentor.

Based on the resume

Suggest

Career Path

Technologies to Learn

Weak Areas

Strengths

Next 6 Month Roadmap

"""

REWRITE_PROMPT = """
Rewrite the resume professionally.

Improve

Grammar

Action Verbs

Sentence Structure

Technical Writing

ATS Compatibility

Do NOT add fake information.

"""

RAG_PROMPT = """
Answer the question ONLY using the retrieved resume context.

If the answer is not found,

reply

"I could not find that information in the resume."

Never hallucinate.

"""

