from flask import Flask,render_template,request
import instaloader
import zip 
import os
import config as co


app = Flask(__name__)

@app.route("/")
def main1():
    return render_template("main.html")

def download_instagram_post(url, defult_folder):
    defult_folder= defult_folder+co.get_config("target_substring")
    dir="./posts"
    
    target_path = os.path.join(dir,defult_folder )
    L = instaloader.Instaloader(dirname_pattern=target_path)
    try:
        # Download the post by URL
        post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
        filename = f"{post.date_utc}_{post.owner_username}_inst"
        L.download_post(post, target=filename)
        print("Post downloaded successfully in folder:", defult_folder)
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")

@app.route('/responses', methods=['POST'])
def responses():
    if request.method == 'POST':
        url = request.form['url']
        defult_folder = co.get_config("defult_folder")
        checkbox_value = request.form.get('new_folder')
        print(checkbox_value)
        
        if checkbox_value:
            val = request.form['folder']
            defult_folder = val
        
        
        print(defult_folder)
        
        download_instagram_post(url, defult_folder)
        return {
            "message": "Download request received successfully."
        }

    
@app.route('/zip', methods=['GET','POST'])
def zip_backup():
    base_directory = co.get_config("base_directory")
    target_substring = co.get_config("target_substring")
    result = zip.find_folder_with_string(base_directory, target_substring)
    
    
    backup_folder=zip.create_backup_folder()
    # zip_folder(folder_path, zip_name)
    for i in result:
        folder_to_zip = i
        zip_filename = os.path.join(backup_folder, f"{os.path.basename(i)}.zip")
        zip.zip_folder(folder_to_zip, zip_filename)
    return{
        "message":"all ok",
        "folder":"back_up done"
    }

if __name__ == '__main__':
   app.run(debug = True)