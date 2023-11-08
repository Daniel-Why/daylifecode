# 支持提取文件夹内由Axure生成原型的HTML文件，并生成索引index页面
import os
import fnmatch


def find_html_files(directory):
    all_projects = []
    exclude_filename = ["index.html", "start.html", "start_c_1.html","start_with_pages.html"]
    exclude_dirnames = ["resources", "data", "files", "images", "plugins"]
    for root, dirnames, filenames in os.walk(directory):
        if any(value in root for value in exclude_dirnames):
            continue
        else:
            project=[]
            html_files = []
            print(root)
            project.append(root[2:])
            for filename in fnmatch.filter(filenames, "*.html"):
                if filename not in exclude_filename:
                    html_files.append(os.path.join(root, filename))
            project.append(html_files)
            all_projects.append(project)
    return all_projects


def create_index_html(output_file, all_projects):
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<title>原型目录</title>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("<h1>原型目录</h1>\n")
        for project in all_projects:
            f.write(f"<h2>{project[0]}</h2><br>\n")
            for html_file in project[1]:
                f.write(f"<a href='{html_file}' target='_blank'>{html_file}</a><br>\n")
        f.write("</body>\n")
        f.write("</html>\n")


def main():
    html_files = find_html_files("./")  # 将这里替换为你的目录路径
    output_file = "./index.html"  # 将这里替换为你想要生成的 index 文件的路径和名称
    create_index_html(output_file, html_files)


if __name__ == "__main__":
    main()
