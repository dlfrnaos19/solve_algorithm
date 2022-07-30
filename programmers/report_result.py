from collections import Counter

id_list = ["con", "ryan"]
result_list = [0] * len(id_list)
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

report = set(report)
report_list = []
for repo in report:
    user, report_user = repo.split()
    report_list.append(report_user)

report_counter = Counter(report_list)
block_list = []
for user,n_report in report_counter.items():
    if n_report >= k:
        print(user,"는 block 대상")
        block_list.append(user)

for idx, repo in enumerate(report):
    user, report_user = repo.split()
    if report_user in block_list:
        user_idx = id_list.index(user)
        result_list[user_idx] = result_list[user_idx]+1
print(result_list)

        