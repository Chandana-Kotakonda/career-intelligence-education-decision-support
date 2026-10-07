# Data Dictionary

This document defines the important fields used in the
Career Intelligence & Education Decision Support System.

## Career Taxonomy

### career_id
Unique identifier assigned to each career.

### career_name
Name of the career or occupation.

### career_family
Broad category to which the career belongs, such as Technology,
Finance, Healthcare, Engineering, Management, Law, Science,
Education, Design, Agriculture, Hospitality, Media, Defence,
Government, or Aviation.

### description
Short explanation of the career. This field will be added or
expanded when the career knowledge base is developed.

### source
Indicates where the career information originated.

### last_verified
Date on which the career information was last checked or verified.

## User Profile

### user_id
Unique identifier for a user profile.

### education
User's current or completed education level.

### skills
Skills currently possessed by the user.

### interests
User's stated areas of interest.

### experience
Relevant experience or background provided by the user.

### career_goal
Career direction or goal specified by the user.

## Recommendation

### match_score
Numerical score representing how well a career matches the
user's profile.

### matched_skills
Skills from the user's profile that match the career requirements.

### skill_gaps
Important skills required by the career that are missing or
underrepresented in the user's profile.

### recommendation_reason
Human-readable explanation describing why a career was recommended.

## Job Market

### job_id
Unique identifier for a job posting.

### title
Title of the job posting.

### description
Full or summarized job description.

### location
Location associated with the job posting.

### work_type
Type of work arrangement, such as full-time, part-time,
contract, or other available categories.

### job_posting_url
URL of the original job posting.

## Education

### institution
Name of the educational institution.

### programme
Name of the academic programme.

### discipline
Academic discipline or field of study.

### enrollment
Number of students enrolled in the relevant category.

### state
State or union territory associated with the education data.

## Data Governance

### source
Original source of the information.

### last_verified
Date when the information was most recently checked.

These fields may be expanded as the project develops and
additional analytical tables are created.