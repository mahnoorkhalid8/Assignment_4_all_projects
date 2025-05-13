import requests
import streamlit as st

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    res = requests.get(url)
    
    if res.status_code == 200:
        user_data = res.json()
        
        name = user_data.get("name", "No name found")
        bio = user_data.get("bio", "No bio found")
        avatar_url = user_data.get("avatar_url", "")
        repos_url = user_data.get("repos_url", "")  # ✅ correct key
        followers = user_data.get("followers", 0)
        following = user_data.get("following", 0)
        public_repos = user_data.get("public_repos", 0)  # ✅ correct key
        company = user_data.get("company", "Not available")
        location = user_data.get("location", "Not available")
        blog = user_data.get("blog", "Not available")
        
        repo_response = requests.get(repos_url)
        if repo_response.status_code == 200:
            repo_data = repo_response.json()
            repo_list = [(repo["name"], repo["html_url"]) for repo in repo_data]
        else:
            repo_list = []
            
        return {
            "name": name,
            "bio": bio,
            "avatar_url": avatar_url,
            "repo": repo_list,
            "followers": followers,
            "following": following,
            "public_repos": public_repos,
            "company": company,
            "location": location,
            "blog": blog
        }
    else:
        return None

# --- Streamlit UI ---
st.title("GitHub Profile Information")
username = st.text_input("Enter GitHub username: ")

if username:
    user_data = get_github_user(username)
    
    if user_data:
        st.subheader(f"Name: {user_data['name']}")
        st.write(f"Bio: {user_data['bio']}")
        st.image(user_data["avatar_url"], caption="Profile Image", width=150)
        
        st.subheader("User Details:")
        st.write(f"Followers: {user_data['followers']}")
        st.write(f"Following: {user_data['following']}")
        st.write(f"Public Repositories: {user_data['public_repos']}")
        st.write(f"Company: {user_data['company']}")
        st.write(f"Location: {user_data['location']}")
        st.write(f"Blog: {user_data['blog']}")
        
        st.subheader("Repositories:")
        if user_data["repo"]:
            for repo_name, repo_url in user_data["repo"]:
                st.markdown(f"- [{repo_name}]({repo_url})")
        else:
            st.write("No repositories found.")
    else:
        st.error("User not found. Please check the username and try again.")
