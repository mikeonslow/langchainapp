from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
import json


def main():
    print("starting application...")

    linkedin_profile_url = linkedin_lookup_agent(name="Erin Onslow")

    summary_template = """
    given the {information} about a person from I want you to create
    1. a short summary
    2. 10 Interview questions for them
    3. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # with open("/app/output/ice_breaker.txt", "w") as f:
    #     f.write("Hello LangChain!")

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url, is_mock=False
    )

    print(chain.run(information=linkedin_data))


# json_data = {'public_identifier': 'mikeonslow', 'profile_pic_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/person/mikeonslow/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230523%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230523T044708Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=ca52771a3d14aee35cc396a43233c775d8fc6ae7a2b562d4f7d61bf3ab18a2cf', 'first_name': 'Mike', 'last_name': 'Onslow', 'full_name': 'Mike Onslow', 'headline': '\n                  Principal Software Engineer at Clarity Voice\n              ', 'summary': 'I am a full stack software engineer & architect with over 10 years of experience in the field. I love solving problems and have a passion for creating great web applications that make life better for those around me!\n\nCurrently, I work for a premier cloud based Unified  Communications Provider and focus on heading up our software systems division. \n\nI am also very involved in the software engineering community and have a thirst for knowledge. I love to push forth into learning, evaluating and possibly implementing promising technologies to stay ahead of the game.', 'country': 'US', 'city': 'Farmington', 'state': 'Michigan', 'experiences': [{'starts_at': None, 'ends_at': None, 'company': 'Shadow Technologies, L.L.C.', 'company_linkedin_profile_url': None, 'title': 'Senior IT Specialist', 'description': None, 'location': 'Rochester Hills, MI', 'logo_url': None}, {'starts_at': None, 'ends_at': None, 'company': 'Siteworks Web Studios', 'company_linkedin_profile_url': None, 'title': 'Web Application Developer', 'description': None, 'location': 'Ferndale, MI', 'logo_url': None}, {'starts_at': None, 'ends_at': None, 'company': 'Clarity Voice', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/clarity-voice', 'title': 'Principal Software Engineer', 'description': None, 'location': 'Southfield', 'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/clarity-voice/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230523%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230523T044708Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=0cdc492ba4c29377dfb7ece71af0bfe3758bde0d6cd68c2073e4071a36ee4ef3'}, {'starts_at': None, 'ends_at': None, 'company': 'Clarity Voice', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/clarity-voice', 'title': 'Application Developer', 'description': None, 'location': 'Southfield, MI', 'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/clarity-voice/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230523%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230523T044708Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=0cdc492ba4c29377dfb7ece71af0bfe3758bde0d6cd68c2073e4071a36ee4ef3'}, {'starts_at': None, 'ends_at': None, 'company': 'Concise Computer Consulting', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/concise-computer-consulting', 'title': 'Lead IT Specialist', 'description': None, 'location': 'Bloomfield Hills, Michigan', 'logo_url': None}, {'starts_at': None, 'ends_at': None, 'company': 'Hubbell, Roth & Clark', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/hubbell-roth-&-clark', 'title': 'Network Support Analyst', 'description': None, 'location': 'Bloomfield Hills, Michigan', 'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/hubbell-roth-%26-clark/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230523%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230523T044708Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=5fe8f1d6dbee9ac6ab3b379370ded8b00d1186811319adc64aee5fe4f315febf'}, {'starts_at': None, 'ends_at': None, 'company': 'SKF Groupe', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/skf', 'title': 'Computer Systems Analyst', 'description': None, 'location': 'Farmington Hills, MI', 'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/skf/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230523%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230523T044708Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=7740d01dfad58c1cfb0c601fddf88996788353a245b0e0a30508b5701530a4b4'}], 'education': [{'starts_at': None, 'ends_at': None, 'field_of_study': '4.0', 'degree_name': 'Information Systems', 'school': 'Oakland Community College', 'school_linkedin_profile_url': 'https://www.linkedin.com/school/oakland-community-college/', 'description': None, 'logo_url': None, 'grade': None, 'activities_and_societies': None}], 'social_networking_services': [{'service': 'stackoverflow', 'canonical_url': 'stackoverflow.com/users/2188152', 'internal_id': '2188152'}]}

# json_object = json.loads(json_data)

# print(linkedin_data)


if __name__ == "__main__":
    main()
