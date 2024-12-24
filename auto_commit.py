import os
import time
import random
from datetime import datetime
from github import Github
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# GitHub configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError("Please set GITHUB_TOKEN in .env file")

gh = Github(GITHUB_TOKEN)
user = gh.get_user()

# Daftar nama repo yang menarik
REPO_PREFIXES = [
    "python-project", "web-app", "data-analysis",
    "learning", "tutorial", "tools", "automation",
    "study-notes", "playground", "experiment"
]

# Daftar topik untuk konten
TOPICS = [
    "Python Programming", "Web Development", "Data Science",
    "Machine Learning", "Software Engineering", "Cloud Computing",
    "DevOps", "Automation", "Best Practices", "Tips and Tricks"
]

def generate_repo_name():
    """Generate nama repo yang lebih natural"""
    prefix = random.choice(REPO_PREFIXES)
    suffix = ''.join(random.choices('0123456789', k=3))
    return f"{prefix}-{suffix}"

def generate_content():
    """Generate konten yang lebih menarik dan bervariasi"""
    topic = random.choice(TOPICS)
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    content = f"""# {topic} Project

## Overview
Repository ini berisi pembelajaran dan eksperimen saya tentang {topic.lower()}.

## Konten
- Implementasi best practices
- Contoh kode dan tutorial
- Dokumentasi pembelajaran
- Catatan pengembangan

## Update Terakhir
Diperbarui pada: {current_date}

## Tujuan
- Meningkatkan pemahaman tentang {topic.lower()}
- Berbagi pengetahuan dengan komunitas
- Dokumentasi pembelajaran personal
- Implementasi konsep-konsep penting

## Kontribusi
Silakan berkontribusi dengan membuat pull request atau membuka issue.

## Lisensi
MIT License
"""
    return content

def create_repo():
    """Create a new repository with interesting name and content"""
    repo_name = generate_repo_name()
    try:
        repo = user.create_repo(repo_name, private=False, 
                              description=f"A project about {random.choice(TOPICS).lower()}")
        print(f"Created repository: {repo_name}")
        return repo
    except Exception as e:
        print(f"Error creating repository: {e}")
        return None

def make_commit():
    """Create a new repository and make a commit with interesting content"""
    repo = create_repo()
    if not repo:
        return
    
    try:
        # Create README.md with interesting content
        content = generate_content()
        repo.create_file("README.md", "Initial commit with project structure", content)
        
        # Add some example code files
        example_code = """def hello_world():
    print("Hello, World!")
    
if __name__ == "__main__":
    hello_world()
"""
        repo.create_file("example.py", "Add example code", example_code)
        print(f"Made commit to {repo.name} with interesting content")
    except Exception as e:
        print(f"Error making commit: {e}")

def main():
    """Main function to run the auto commit process"""
    print("Starting commit process...")
    while True:
        make_commit()
        
        # Random delay between 2-4 jam untuk terlihat lebih natural
        delay = random.randint(7200, 14400)
        print(f"Waiting {delay//3600} hours before next commit...")
        time.sleep(delay)

if __name__ == "__main__":
    main() 