from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
import json

information = """

Elon Reeve Musk FRS (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. He is the founder, CEO and chief engineer of SpaceX; angel investor, CEO and product architect of Tesla, Inc.; owner and CEO of Twitter, Inc.; founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the philanthropic Musk Foundation. Musk is the second-wealthiest person in the world, according to both the Bloomberg Billionaires Index and Forbes's Real Time Billionaires list as of May 2023 primarily from his ownership stakes in Tesla and SpaceX, with an estimated net worth of around $167 billion according to the Bloomberg and $176.2 billion according to the latter.[4][5][6][7]

Musk was born in Pretoria, South Africa, and briefly attended the University of Pretoria before moving to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University and transferred to the University of Pennsylvania, where he received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University. After two days, he dropped out and, with his brother Kimbal, co-founded the online city guide software company Zip2. In 1999, Zip2 was acquired by Compaq for $307 million and Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal, which eBay acquired for $1.5 billion in 2002.

With $175.8 million, Musk founded SpaceX in 2002, a spaceflight services company. In 2004, he was an early investor in the electric vehicle manufacturer Tesla Motors, Inc. (now Tesla, Inc.). He became its chairman and product architect, assuming the position of CEO in 2008. In 2006, he helped create SolarCity, a solar energy company that was later acquired by Tesla and became Tesla Energy. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, he co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and the Boring Company, a tunnel construction company. Musk has also proposed a hyperloop high-speed vactrain transportation system. In 2022, his acquisition of Twitter for $44 billion was completed.

Musk has expressed views that have made him a polarizing figure. He has been criticized for making unscientific and misleading statements, including spreading COVID-19 misinformation, and has been accused of antisemitism. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk for falsely tweeting that he had secured funding for a private takeover of Tesla. Musk stepped down as chairman of Tesla and paid a $20 million fine as part of a settlement agreement with the SEC.

Early life
Childhood and family
Further information: Musk family
Elon Reeve Musk was born on June 28, 1971, in Pretoria, one of South Africa's capital cities.[8][9] Musk has British and Pennsylvania Dutch ancestry.[10][11] His mother is Maye Musk (née Haldeman), a model and dietitian born in Saskatchewan, Canada, and raised in South Africa.[12][13][14] His father, Errol Musk, is a South African electromechanical engineer, pilot, sailor, consultant, and property developer, who partly owned a Zambian emerald mine near Lake Tanganyika.[15][16][17][18] Musk has a younger brother, Kimbal, and a younger sister, Tosca.[14][19]

Musk's family was wealthy during his youth.[18] His father was elected to the Pretoria City Council as a representative of the anti-apartheid Progressive Party and has said that his children shared their father's dislike of apartheid.[8] His maternal grandfather, Joshua Haldeman, was an adventurous American-born Canadian who took his family on record-breaking journeys to Africa and Australia in a single-engine Bellanca airplane.[20][21][22] After his parents divorced in 1980, Musk chose to mostly live with his father.[10] Musk regretted his decision and has become estranged from his father.[23] He has a paternal half-sister and a half-brother.[20][24]

Maye Musk has said of her son that he "was shy and awkward at school" and "didn't have many friends".[25] At age ten, he developed an interest in computing and video games, teaching himself how to program from the VIC-20 user manual.[26] At age twelve, he sold his BASIC-based game Blastar to PC and Office Technology magazine for approximately $500.[27][28]

Education
An ornate school building
Musk graduated from Pretoria Boys High School in South Africa.
Musk attended Waterkloof House Preparatory School, Bryanston High School, and Pretoria Boys High School, from which he graduated.[29] Musk applied for a Canadian passport through his Canadian-born mother,[30][31] knowing that it would be easier to immigrate to the United States this way.[32] While waiting for his application to be processed, he attended the University of Pretoria for five months.[33]

Musk arrived in Canada in June 1989 and lived with a second cousin in Saskatchewan for a year,[34] working odd jobs at a farm and lumber mill.[35] In 1990, he entered Queen's University in Kingston, Ontario.[36][37] Two years later, he transferred to the University of Pennsylvania (UPenn), where he completed studies for a Bachelor of Arts degree in physics and a Bachelor of Science degree in economics from the Wharton School.[38][39][40][41] Although Musk claims he earned the degrees in 1995, UPenn maintains it awarded them in 1997.[42] He reportedly hosted large, ticketed house parties to help pay for tuition, and wrote a business plan for an electronic book-scanning service similar to Google Books.[43]

In 1994, Musk held two internships in Silicon Valley: one at the energy storage startup Pinnacle Research Institute, which investigated electrolytic ultracapacitors for energy storage, and another at the Palo Alto–based startup Rocket Science Games.[44][45] In 1995, he was accepted to a PhD program in materials science at Stanford University.[46][47] However, Musk decided to join the Internet boom, instead dropping out two days after being accepted and applied for a job at Netscape, to which he reportedly never received a response.[48][30]

Business career
Zip2
Main article: Zip2
External video
video icon Musk speaks of his early business experience during a 2014 commencement speech at USC on YouTube
In 1995, Musk, his brother Kimbal, and Greg Kouri founded Zip2.[49][50] Errol Musk provided them with $28,000 in funding.[51] The company developed an Internet city guide with maps, directions, and yellow pages, and marketed it to newspapers.[52] They worked at a small rented office in Palo Alto,[53] Musk coding the website every night.[53] Eventually, Zip2 obtained contracts with The New York Times and the Chicago Tribune.[43] The brothers persuaded the board of directors to abandon a merger with CitySearch;[54] however, Musk's attempts to become CEO were thwarted.[55] Compaq acquired Zip2 for $307 million in cash in February 1999,[56][57] and Musk received $22 million for his 7-percent share.[58]

X.com and PayPal
Main articles: X.com, PayPal, and PayPal Mafia
Later in 1999, Musk co-founded X.com, an online financial services and e-mail payment company.[59] X.com was one of the first federally insured online banks, and over 200,000 customers joined in its initial months of operation.[60] Even though Musk founded the company, investors regarded him as inexperienced and replaced him with Intuit CEO Bill Harris by the end of the year.[61]

In 2000, X.com merged with online bank Confinity to avoid competition,[53][61][62] as Confinity's money-transfer service PayPal was more popular than X.com's service.[63] Musk then returned as CEO of the merged company. His preference for Microsoft over Unix-based software caused a rift among the company's employees, and led Peter Thiel, Confinity's founder, to resign.[64] With the company suffering from compounding technological issues and the lack of a cohesive business model, the board ousted Musk and replaced him with Thiel in September 2000.[65][b] Under Thiel, the company focused on the money-transfer service and was renamed PayPal in 2001.[67][68]

In 2002, PayPal was acquired by eBay for $1.5 billion in stock, of which Musk—the largest shareholder with 11.72% of shares—received $175.8 million.[69][70] In 2017, more than 15 years later, Musk purchased the X.com domain from PayPal for its sentimental value.[71][72] In 2022, Musk discussed a goal of creating "X, the everything app".[73]


"""


def main():
    print("starting application...")

    # summary_template = """
    # given the {information} about a person from I want you to create
    # 1. a short cummary
    # 2. two interesting facts about them
    # """

    # summary_prompt_template = PromptTemplate(
    #     input_variables=["information"], template=summary_template
    # )

    # llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # # with open("/app/output/ice_breaker.txt", "w") as f:
    # #     f.write("Hello LangChain!")

    # print(chain.run(information=information))


linkedin_data = scrape_linkedin_profile(
    linkedin_profile_url="https://www.linkedin.com/in/mikeonslow/"
)

# json_data = {'public_identifier': 'mikeonslow', 'profile_pic_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/person/mikeonslow/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230523%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230523T044708Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=ca52771a3d14aee35cc396a43233c775d8fc6ae7a2b562d4f7d61bf3ab18a2cf', 'first_name': 'Mike', 'last_name': 'Onslow', 'full_name': 'Mike Onslow', 'headline': '\n                  Principal Software Engineer at Clarity Voice\n              ', 'summary': 'I am a full stack software engineer & architect with over 10 years of experience in the field. I love solving problems and have a passion for creating great web applications that make life better for those around me!\n\nCurrently, I work for a premier cloud based Unified  Communications Provider and focus on heading up our software systems division. \n\nI am also very involved in the software engineering community and have a thirst for knowledge. I love to push forth into learning, evaluating and possibly implementing promising technologies to stay ahead of the game.', 'country': 'US', 'city': 'Farmington', 'state': 'Michigan', 'experiences': [{'starts_at': None, 'ends_at': None, 'company': 'Shadow Technologies, L.L.C.', 'company_linkedin_profile_url': None, 'title': 'Senior IT Specialist', 'description': None, 'location': 'Rochester Hills, MI', 'logo_url': None}, {'starts_at': None, 'ends_at': None, 'company': 'Siteworks Web Studios', 'company_linkedin_profile_url': None, 'title': 'Web Application Developer', 'description': None, 'location': 'Ferndale, MI', 'logo_url': None}, {'starts_at': None, 'ends_at': None, 'company': 'Clarity Voice', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/clarity-voice', 'title': 'Principal Software Engineer', 'description': None, 'location': 'Southfield', 'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/clarity-voice/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230523%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230523T044708Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=0cdc492ba4c29377dfb7ece71af0bfe3758bde0d6cd68c2073e4071a36ee4ef3'}, {'starts_at': None, 'ends_at': None, 'company': 'Clarity Voice', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/clarity-voice', 'title': 'Application Developer', 'description': None, 'location': 'Southfield, MI', 'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/clarity-voice/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230523%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230523T044708Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=0cdc492ba4c29377dfb7ece71af0bfe3758bde0d6cd68c2073e4071a36ee4ef3'}, {'starts_at': None, 'ends_at': None, 'company': 'Concise Computer Consulting', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/concise-computer-consulting', 'title': 'Lead IT Specialist', 'description': None, 'location': 'Bloomfield Hills, Michigan', 'logo_url': None}, {'starts_at': None, 'ends_at': None, 'company': 'Hubbell, Roth & Clark', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/hubbell-roth-&-clark', 'title': 'Network Support Analyst', 'description': None, 'location': 'Bloomfield Hills, Michigan', 'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/hubbell-roth-%26-clark/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230523%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230523T044708Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=5fe8f1d6dbee9ac6ab3b379370ded8b00d1186811319adc64aee5fe4f315febf'}, {'starts_at': None, 'ends_at': None, 'company': 'SKF Groupe', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/skf', 'title': 'Computer Systems Analyst', 'description': None, 'location': 'Farmington Hills, MI', 'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/skf/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230523%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230523T044708Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=7740d01dfad58c1cfb0c601fddf88996788353a245b0e0a30508b5701530a4b4'}], 'education': [{'starts_at': None, 'ends_at': None, 'field_of_study': '4.0', 'degree_name': 'Information Systems', 'school': 'Oakland Community College', 'school_linkedin_profile_url': 'https://www.linkedin.com/school/oakland-community-college/', 'description': None, 'logo_url': None, 'grade': None, 'activities_and_societies': None}], 'social_networking_services': [{'service': 'stackoverflow', 'canonical_url': 'stackoverflow.com/users/2188152', 'internal_id': '2188152'}]}

# json_object = json.loads(json_data)

print(linkedin_data)


if __name__ == "__main__":
    main()
