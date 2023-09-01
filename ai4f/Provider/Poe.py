from re import search
from time import sleep
from httpx import Client
import json
import secrets, string

from curl_cffi import requests

from .base_provider import BaseProvider
from ..typing import CreateResult, Any

class Poe(BaseProvider):
    url = "https://poe.com/"
    working = True
    supports_gpt_35_turbo = True
    supports_stream = True
    needs_auth = True
    supports_gpt_4 = True

    @staticmethod
    def create_completion(
        model: str,
        messages: list[dict[str, str]],
        stream: bool,
        **kwargs: Any,
    ) -> CreateResult:
        client = PoeApi(cookie=kwargs.get('auth'))
        client.get_chat_history(models[model])
        result = client.send_message(models[model],messages)
        yield result['response'].strip()

    @classmethod
    @property
    def params(cls):
        params = [
            ("model", "str"),
            ("messages", "list[dict[str, str]]"),
            ("stream", "bool"),
            ("temperature", "float"),
        ]
        param = ", ".join([": ".join(p) for p in params])
        return f"g4f.provider.{cls.__name__} supports: ({param})"
    

models = {
    'sage-assistant': 'capybara',
    'claude-instant-v1-100k': 'a2_100k',
    'claude-v2-100k': 'a2_2',
    'claude-instant-v1': 'a2',
    'gpt-3.5-turbo':'chinchilla',
    'gpt-3.5-turbo-16k': 'agouti',
    'gpt-4': 'beaver',
    'gpt-4-32k': 'vizcacha',
    'palm': 'acouchy',
    'llama-2-7b': 'llama_2_7b_chat',
    'llama-2-13b': 'llama_2_13b_chat',
    'llama-2-70b': 'llama_2_70b_chat',
}

QUERIES = {
  "AddEmailMutation": "6d9ff3c8ed7badced30cfdad97492d4c21719931e8c44c5601abfa429b62ded7",
  "ChatHelpers_addMessageBreakEdgeMutation_Mutation": "9450e06185f46531eca3e650c26fa8524f876924d1a8e9a3fb322305044bdac3",
  "AddPhoneNumber": "26ae865f0686a910a86759c069eb1c0085d78b55a8abf64444ec63b03c76fb58",
  "AnnotateWithIdsProviderQuery": "b4e6992c3af8f208ab2b3979dce48889835736ed29f623ea9f609265018d0d8f",
  "AvailableBotsListModalPaginationQuery": "3be373baa573ccd196b9d71c94953b1d1bc586625bd64efe51655d75e68bbfb7",
  "AvailableBotsSelectorModalPaginationQuery": "dd9281852c9a4d9d598f5a215e0143a8f76972c08e84053793567f7a76572593",
  "BotInfoFormRunCheckMutation": "87d55551061151b852fd7c53ec34dbb1ae784516b0ba2df5255b201f0d4e1444",
  "BotInfoModalQuery": "33254e9e91d63d16dbac1d70aa6accfb31786be05f7749772a32bc37d9ccb799",
  "BotLandingPageQuery": "fb2f3e506be25ff8ba658bf55cd2228dec374855b6758ec406f0d1274bf5588d",
  "BotSelectorModalQuery": "b1ed351177d82da55670039a971c647b87874d28c5e137b8eb9c9fdf7fb30f7b",
  "BotSwitcherModalQuery": "54023ee8b691543982b2819491532532c317b899918e049617928137c26d47f5",
  "ChatDeleteConfirmationModalQuery": "716c8cc3ac6c13d6b41ceb2404e3a28c63aea6d166bf071dca1f98e0377727c3",
  "ChatHelpersSendNewChatMessageMutation": "943e16d73c3582759fa112842ef050e85d6f0048048862717ba861c828ef3f82",
  "ChatHistoryFilteredListPaginationQuery": "ea1894d73aa8a16d059c56696305c85761b11822f4f60e6471d1e24cb14100cf",
  "ChatHistoryListPaginationQuery": "9d52c1995f77c6f9a8c93956dbf79f4ab1024f5bfb797118727b29fed81eee7f",
  "ChatHomeMainInputContainerOptimisticBotQuery": "1c9267ecff73cb27a8e7d94a3f5b5fe665a82abe0fdd61be2e54dd38c0e61639",
  "ChatHomeMainInputContainerOptimisticViewerQuery": "21f0eb43ab07d97d4a30bcf007db4797b95e852fb6537e8dbbc002da45ba4fac",
  "ChatListPaginationQuery": "dc3f4d34f13ed0a22b0dbfa6a1924a18922f7fe3a392b059b0c8c2134ce4ec8a",
  "ChatLoaderQuery": "d9467ac216e21b510eb8e72a2888289d173c9d5ce399b072fd88bee3da1b1459",
  "ChatPageBotBotsPagination": "ed9017f85fe2fedbf02b2d000cb4b551d2ec870715d0c7bce6d54a0f3f9b657b",
  "ChatPageQuery": "63eee0aafc4d83a50fe7ceaec1853b191ea86b3d561268fa7aad24c69bb891d9",
  "hatsHistoryPageQuery": "050767d78f19014e99493016ab2b708b619c7c044eebd838347cf259f0f2aefb",
  "ChatSetTitle": "24574aab7fedf86d1654bbc70bf5421abbc33e195aa1c11178697023a27a912e",
  "ChatSettingsModalQuery": "41910ff112abaa713edd836cbb7fc567433f3f7ac3a61659fffca6306f7288ac",
  "ChatSubscriptionPaywallModalQuery": "559ac4c7c8f0f6f50148d255bb6318107034375df7bca4214f608cd65b573a21",
  "ChatSwitcherRefetchQuery": "815b8e6406bd19b25da36523b8b33c8c25e6db2fe93505117bb583c2d9dd60e4",
  "ChatTitleUpdated": "740e2c7ab27297b7a8acde39a400b932c71beb7e9b525280fc99c1639f1be93a",
  "ChatsHistoryPageQuery": "050767d78f19014e99493016ab2b708b619c7c044eebd838347cf259f0f2aefb",
  "ContinueChatFromPoeShare": "a220810c2d1d3b5284b6be44309a3d2b197c312a79b1a27f165a12f1508322bd",
  "ContinueChatIndexPageQuery": "a7eea6eebd14aa355723514558762315d0b4df46205b70f825d288d5ed1635ec",
  "ContinueChatPageQuery": "fe3a4d2006b1c4bb47ac6dea0639bc9128ad983cf37cbc0006c33efab372a19d",
  "CreateBotIndexPageQuery": "6bd24eb031dd0d427ddeef0c4113d9b3800aa44b62aed25143d6a95251765e38",
  "CreateBotPageQuery": "4fa5e0703c416fc6b40c5e2fcfcac66301ed0c8d32bafb5d69300e7553ef1f8f",
  "CreateChatMutation": "f1322c9c34d4140d420aeb9151cdeebc2235d381ada0037c845572310f613b7d",
  "CreateChatWithTitle": "6cf8cddd6594901bd4a7dc6ddeffc91485c21c817e8f7fa07fae9d71d9807d71",
  "CreateCheckoutSession": "5eb43e7c83974acc6680e1abe4c169296d0b346c42cc20d487762163402ea8e5",
  "CreateCustomerPortalSession": "4d43136f33aba6b6dea2ac8cd295e03bd841b7c99bf772940fa06a623a331786",
  "CreateMessagesToContinueChatMutation": "00b66f0117fab1ab6cdcf7e98819c1e3196736253b6a158316a49f587b964d25",
  "DeleteAccountMutation": "4e9651277464843d4d42fbfb5b4ccb1c348e3efe090d6971fa7a3c2cabc7ea5c",
  "DeleteChat": "5df4cb75c0c06e086b8949890b1871a9f8b9e431a930d5894d08ca86e9260a18",
  "DeleteMessageMutation": "8d1879c2e851ba163badb6065561183600fc1b9de99fc8b48b654eb65af92bed",
  "DeleteUserMessagesMutation": "3f60d527c3f636f308b3a26fc3a0012be34ea1a201e47a774b4513d8a1ba8912",
  "DismissDismissible": "b133084411c0a7a2353f6cfacd3d115260c34ddc5d97cf7f19a16e8cb4410803",
  "EditBotIndexPageQuery": "52c3db81cca5f44ae4de3705633488511bf7baa773c3fe2cb16b148f5b5cf55e",
  "EditBotPageQuery": "67c96902edcb66854106892671c816d9f7c3d8910f5a6b364f8b9f3c2bc7a37a",
  "EmailUnsubscribe": "eacf2ae89b7a30460619ccfb0d5a4e6007cfbcf0286ec7684c24192527a00263",
  "EmbedLoggedOutPageQuery": "e81580f4126215186e8a5d18bdedcf7c056b634d4d864f54b948765c8c21aef9",
  "ExploreBotsCarouselContainerQuery": "e46511b51cb2e9244225e1e6509c6a696dde271e45da74ce66853379eaeb80d6",
  "ExploreBotsCarouselLazyLoadedContainerQuery": "846522f24edbbad1331cedfe311ba0c8e365cf33aee1bb1e3f0e03156f1a0536",
  "ExploreBotsCarouselPagedContainerPaginationQuery": "619df00e336f6bbad2bbc2626aa74f97eb12efb50f403339cc780041aa9897e0",
  "ExploreBotsIndexPageQuery": "78bf0e0de2b2af5608ca5a58bfdacbb5633cd44e1d26477b26c5a519535d5dc4",
  "ExploreBotsListPaginationQuery": "983be13fda71b7926b77f461ae7e8925c4e696cdd578fbfd42cb0d14103993ac",
  "ExploreBotsPageQuery": "be8c7ca9725a477d6b04f907f3c0f0f58dd7647550555811720ffbac3c90ecfb",
  "ExploreBotsSidebarQuery": "00f42e3842c63cfcfcebad6402cdaa1df1c3fa7ffe3efbe0437a08a151eca87e",
  "GenerateAppleAuthNonceMutation": "c3e0c1b990cd17322716d0fa943a8ddc0ffecf45294ad013ccc883954c2171fc",
  "HandleBotChatEmbedPageQuery": "60a48e1b772e6830ddbdb54f19e837beef949d4fc146c51b1f50469f40b7650b",
  "HandleBotChatPageQuery": "dc1891a1d9b3ca42c773a69e9985f95e78a13ad5858cef0574c7f4ce87004a77",
  "HandleProfileIndexPageQuery": "0243e1784c33ae913d8a3ad20fc1252b930b6741ff9d78bd776e2df4f93f55ee",
  "HandleProfilePageQuery": "4605a49a28aa5647b96f437d61a8b9318e2619d9974c61759b0ec82b201befb7",
  "IntroMainQuery": "47f2c9bb41be5238968c81c82f2d2cff4100c73fcc70a9f592825bb40c0efc8d",
  "LayoutLeftSidebarQuery": "073fc8aad11bae987f5b70a68a0c2fedf8c8b3f2702757cdc68f8aedd1ee8103",
  "LayoutRightSidebarQuery": "ae7498e7255414c3c0bf07a4a8fd16bf880e73995d1046baf882c7119abe6f77",
  "LoginPageQuery": "538d23244211dfe6ed3228518508ebc728f9f8165950d5a19fc5467c2f0b9a1f",
  "LoginWithVerificationCodeMutation": "0d5aecd57239d518c25dc972569ee77dd9610a114610a6a3e87b87fdd8f1ba90",
  "LogoutAllSessionsMutation": "1e62b26302959ca753def8678e817b2c1ad94efdb21872dbf0f8bffcb892aed4",
  "LogoutMutation": "1d2e52b19e15a6aa0ec93d8e4a3a9653b9ceb4c1f365c7d9c4451d835505eef2",
  "MarkAndroidAppDownloadPromptSeen": "ed6891c8913983cc4fd0bfed9760e9738743419712ce6681841217ed0bb8c915",
  "MarkMultiplayerNuxCompleted": "c1b1f2ce72d9f8e9cd7bbe1eecbf6e3bed3366df6a18b179b07ddfd9f1f8b3b1",
  "MessageAdded": "6d5ff500e4390c7a4ee7eeed01cfa317f326c781decb8523223dd2e7f33d3698",
  "MessageCancel": "59b10f19930cf95d3120612e72d271e3346a7fc9599e47183a593a05b68c617e",
  "MessageCancelled": "dfcedd9e0304629c22929725ff6544e1cb32c8f20b0c3fd54d966103ccbcf9d3",
  "MessageDeleted": "91f1ea046d2f3e21dabb3131898ec3c597cb879aa270ad780e8fdd687cde02a3",
  "MessageLimitUpdated": "d862b8febb4c058d8ad513a7c118952ad9095c4ec0a5471540133fc0a9bd3797",
  "MessageUnvoteMutation": "af2b91f09ab2ccf53ba9176a86b9934b98a865adf228b2ac3a548d6397f382f3",
  "MessageVoteMutation": "199fd8402c70ac10c5b05ba31587a0beff3acc39c7194362610ad50bf20299ed",
  "NewLandingPageQuery": "f36fbfcbad84b02876a254ba77ecf78f96360e77291766209b9e7655852440da",
  "NumTokensFromPromptQuery": "1d9bef79811f3b2ddca5ce4027b7eaa31a51bbeed1edf8b6f72e2e0d09d80609",
  "NuxInitialModalQuery": "f8cd0d8494afe3b5dbb349baa28d3ac21f2219ce699e2d59a2345c864905e0c3",
  "NuxInitialModal_poeSetHandle_Mutation": "93a0c939986bb344f87a76d9d709f147a23f1a45ec26e291bcea9acf66b3215f",
  "OnboardingFreeTrialModalQuery": "d2cc659e3def4561ca15b268a97588c5af6cd154afb001312aa69f63c5b2cc9e",
  "OnboardingPaywallModalQuery": "b413e41e89125528f1b2e7f472bde37f6f48a25cb774f4ea3ff883644c973cca",
  "OnboardingPaywallWithGraphicModalQuery": "f986cd3dc4fbab98927983c5d4ed78fa095af78392cf3880af9203dea975890d",
  "OptimisticChatLoaderQuery": "8633378bbe67e397457bebb256d7dc0c48f9a973315f3158cfb2f4fc08ad6c06",
  "PageBlockerQuery": "d1ab792fce4d3f91777b49856d44b2d9cbb6ad1231e1116c407a0208604181e1",
  "PageWrapperQuery": "fa2f44e7aafe6d1698f88ef7443fe13727765570ab504555a15d9c1578ded275",
  "PagesBotNameQuery": "a156136af92b189768540f864445f0b8d9191584530def6b1a5502c843539cfb",
  "PagesDefaultBotChatPageQuery": "75bd0877369c2b4191c936572822ce1875c980f1f6f8683381bd4a6850bdea92",
  "BotInfoCardActionBar_poeBotDelete_Mutation": "ddda605feb83223640499942fac70c440d6767d48d8ff1a26543f37c9bb89c68",
  "BotInfoCardActionBar_poeRemoveBotFromUserList_Mutation": "94f91aa5973c4eb74b9565a2695e422a2ff2afd334c7979fe6da655f4a430d85",
  "PoeBotCreate": "fcc424e9f56e141a2f6386b00ea102be2c83f71121bd3f4aead1131659413290",
  "PoeBotDelete": "c5e5ee2fdac007b02d074ce7882a0631bfbccc73d8833ba8765297c5ea782bb6",
  "PoeBotEdit": "eb93047f1b631df35bd446e0e03555fcc61c8ad83d54047770cd4c2c418f8187",
  "PoeBotFollow": "efa3f25f6cd67f9dea757be50305c0caa6a4e51f52ffba7e4a1c1f2c84d6dbd0",
  "PoeBotUnfollow": "db2281f3efa305db62d38964b640e982076491c2c59d5be3303feae343fe8914",
  "PoeRemoveBotFromUserList": "89e756b668b2318fa73c2a9dde4608a4529c74844667417c0cfb245e7e04e96e",
  "PoeSetBio": "66fb99ec59fa17bc4487f944d116bc920161faced58a3ce99e82cb61af61468e",
  "PoeSetHandle": "4139b28c6a152e2d074944a7cf7f133b453080c1660c4960e14418be363897bb",
  "PoeSetName": "c406a46fe6ff244ab2d665ea953fc8655d6816f1731505d830863d9b9c5021bf",
  "PoeSetProfilePhoto": "13106f2433e5d48a53e6804b76022e80c0fc9bf018eb5b5404d9e0a4acd94f1f",
  "PoeUserSetFollow": "dcc26e4e36b47af8af6bd0296ff85dfa8fc77a9c374ea5989afd0bf39ae4d35e",
  "PostIdPostPageQuery": "653c4768688ce6c8c14ca359ce536646b3de71a7e953c16381136399791c95a0",
  "ProfileIndexPageQuery": "4044ca7eb203e613f19dc76a4a05ca1df25bfdb2ff761a9d6dced6b0d61f219a",
  "ProfilePageQuery": "9505daf59f885463e5bd3bb2a1a9fc088e8634fbc7d5a0682f2ece11ee7548dd",
  "RemoveEmailMutation": "63750a7e41cc0ad3f6da0be1fdae9c243f1afab83cf44bb5c3df14243074681d",
  "RemoveUserPhoneNumberMutation": "7dadad6ac75a8a4e5c54479524c7821e748c043242476958262bb39fa60ccddb",
  "SaveContinueChatInfoMutation": "ae56678376401ae45dbba61aa6b1a55564877edc33605db6283e1dc3bdb0c8ff",
  "SearchResultsListPaginationQuery": "03ce30a457ef8fed9f7677ed642eed8eadd86ca1c7c034f69cb16feb79f5fad2",
  "SearchResultsMainQuery": "b904ab9c97ee1535c1b9b2fa1851b7735f7b4638e535c3230d2a0e235bc78024",
  "SelectorTestPageQuery": "9ec86fe8e3d0d3b264d0fab0feb73e38c86d616c7c3d8340d7a6146bd8445ed3",
  "SendMessageMutation": "5fd489242adf25bf399a95c6b16de9665e521b76618a97621167ae5e11e4bce4",
  "SendVerificationCodeMutation": "d418fa3d2357d089b20065226041180573fa0b0382914a90cf905435281af520",
  "SetPrimaryEmailMutation": "01e75a6d937351b304ca9cc0b231e43587a5923e7f8618863bdf996df38d28b5",
  "SettingsDefaultBotSectionMutation": "4084604e8741af8650ac6b4236cdfa13c91a70cf1c63ad8a368706a386d0887e",
  "SettingsIndexPageQuery": "c9cab56d7329fc2665760ceeb92005e2b3449351a5fb24d906e52587ca87ca64",
  "SettingsPageQuery": "1633485f58c7f2e730a34446b8566c40b5fe2a75ad82b930e3374d8c222b5983",
  "ShareCodeSharePageQuery": "e56f5cb9c7fc9872d053ddaef3dd7827067530b014f59e3ed07bc5e21a0f4334",
  "ShareMessageMutation": "2491190f42c1f5265d8dbaaaf7220dbfa094044fdfb2429fd7f2e35f863bc5e1",
  "SignupOrLoginWithAppleMutation": "649943f9929600796b30f48a47094af56a5d86b4556e34e91aa8ea834cda5fda",
  "SignupOrLoginWithGoogleMutation": "519c2241faeb2bade473ed190913365604eee13ca97b67775b2c7b1aad0fb095",
  "SignupOrLoginWithQuoraMutation": "ee2498e8837e7b975806613401f5aa4ba18d03fdcc9fde0c59efc75717103df5",
  "SignupWallModalInnerQuery": "56f7718c8e586c16065f7b57dcbcf61d3789ab937590e8e77d458613b3c8f325",
  "SignupWithVerificationCodeMutation": "6a9b90b76ee9c058f55a3d659c093a5eca6a5ddbef233dbecee389501b1e5dbf",
  "StaticContentQuery": "15267bf130fbe298a6f60334f57ccf62bc16ff06c74d5778ba54b4b4f21f8d0c",
  "SubscriptionTosQuery": "6696950c5612023d877acd6a6f9026668960994825d3fa71a80528c316510c2f",
  "SubscriptionsMutation": "5a7bfc9ce3b4e456cd05a537cfa27096f08417593b8d9b53f57587f3b7b63e99",
  "UniversalLinkPageQuery": "ec7c629dd6ec79f9d26dda9c4ef9cb1e24aa41d7b92090596b6639eeee5e6cc8",
  "UpdatePhoneNumber": "c49f5f64947c2946f8007f366bbc0ca5b1f0bbbdc6b72ad97be90533f0e83c28",
  "UseBotSelectorBotQuery": "6af7249e90de59baef2e770f7e773f9f7730fd49db6b4e82035c49a078818534",
  "UseBotSelectorViewerBotsPaginationQuery": "e7dbf27efba69f014750ee56ac13f21262e76e161c6e58d435ae75935798d1b0",
  "UseStopMessageAndSendChatBreak": "9b95c61cd6cb41230a51fb360896454dde1ae6d1edb6f075504cb83a52422bc9",
  "UserEditBioModalQuery": "b78089f19d1071ad9440d5a2696588b0e82a012f6b40dca68f071cc0a49727f2",
  "UserEditHandleModalQuery": "ecee1f772c401f6e429ba7ebe088eedc0aa6d24dfa4cae0ec6f54bb3c5a5c653",
  "UserEditNameModalQuery": "dd72d69698a46097386b73b19677a84b6bcba51b3df3790e67d804b6da686787",
  "UserEditProfilePicModalQuery": "7f69ff6407a1360570863b09a9c02bf0a4bdbd8de2b04e5dde4eec031a6f62e5",
  "UserFolloweesListModalQuery": "b219f7e8b7c8d21aaa0979d44bfc3935501719e3fe18cbe86b459eced5f290d2",
  "UserFollowersListModalQuery": "86b007fa15b2de6f7eb527050832d342dde837aaedfb61bfdd1bf1201b860b61",
  "UserProfileConfigurePreviewModalQuery": "abec61f90eebcc3b914487db0ba35ff6ec53c1f7c29f40f59222cee5b8832a52",
  "ViewerStateUpdated": "ee640951b5670b559d00b6928e20e4ac29e33d225237f5bdfcb043155f16ef54",
  "WebSpeedUpsellQuery": "d8556da659d21dc2c583248c1c617ca20492b64c6948ae4a16256c0848f9c32e",
  "WebSubscriptionAnnouncementQuery": "a1b332d7d6816accfccb619e0f0728771ac7c398881fa423051d06551cd0f069",
  "WebSubscriptionPaywallModalQuery": "4d248f3aa4fbf68eb57a1bdda52a6dc5f38dd3b1234c01a95d4b17fdfbd922db",
  "WebSubscriptionPaywallWrapperQuery": "f84fada22609f5dc5933e7ef1e54001fa5e76871836f268e68ad8df7e202f6ca",
}

def generate_payload(query_name, variables) -> str:
    payload = {
        "queryName": query_name,
        "variables": variables,
        "extensions": {
            "hash": QUERIES[query_name]
        }
    }
    return json.dumps(payload, separators=(",", ":"))

def bot_map(bot):
    if bot in models:
        return models[bot]
    return bot.lower().replace(' ', '')
    
def generate_nonce(length:int=16):
      return "".join(secrets.choice(string.ascii_letters + string.digits) for i in range(length))

class PoeApi:
    BASE_URL = 'https://www.quora.com'
    HEADERS = {
        'Host': 'www.quora.com',
        'Accept': '*/*',
        'apollographql-client-version': '1.1.6-65',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Poe 1.1.6 rv:65 env:prod (iPhone14,2; iOS 16.2; en_US)',
        'apollographql-client-name': 'com.quora.app.Experts-apollo-ios',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
    }
    FORMKEY_PATTERN = r'formkey": "(.*?)"'

    def __init__(self, cookie: str, proxy: bool=False):
        if proxy == True:
            proxies = fetch_proxy()
            for p in range(len(proxies)):
                try:
                    self.client = Client(timeout=180, proxies= {"http://": f"{proxies[p]}"})
                    print(f"Connection established with {proxies[p]}")
                    break
                except:
                    print(f"Connection failed with {proxies[p]}. Trying {p+1}/{len(proxies)} ...")
                    sleep(1)
        else:
            self.client = Client(timeout=180)
        self.client.cookies.set('m-b', cookie)
        self.client.headers.update({
            **self.HEADERS,
            'Quora-Formkey': self.get_formkey(),
        })
   
    def __del__(self):
        self.client.close()

    def get_formkey(self):
        response = self.client.get(self.BASE_URL, headers=self.HEADERS, follow_redirects=True)
        formkey = search(self.FORMKEY_PATTERN, response.text)[1]
        return formkey
    
    def send_request(self, path: str, query_name:str="", variables:dict={}):
        payload = generate_payload(query_name, variables)
        response = self.client.post(f'{self.BASE_URL}/poe_api/{path}', data=payload, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        return response.json()
    
    def get_available_bots(self, count: int=25, get_all: bool=False):
        self.bots = {}
        if not (get_all or count):
            raise TypeError(
                "Please provide at least one of the following parameters: get_all=<bool>, count=<int>"
            )
        response = self.send_request('gql_POST',"AvailableBotsSelectorModalPaginationQuery", {}) 
        bots = [
            each["node"]
            for each in response["data"]["viewer"]["availableBotsConnection"]["edges"]
            if each["node"]["deletionState"] == "not_deleted"
        ]
        cursor = response["data"]["viewer"]["availableBotsConnection"]["pageInfo"][
            "endCursor"
        ]
        if len(bots) >= count and not get_all:
            self.bots.update({bot["handle"]: {"bot": bot} for bot in bots})
            return self.bots
        while len(bots) < count or get_all:
            response = self.send_request("gql_POST", "AvailableBotsSelectorModalPaginationQuery", {"cursor": cursor})
            new_bots = [
                each["node"]
                for each in response["data"]["viewer"]["availableBotsConnection"][
                    "edges"
                ]
                if each["node"]["deletionState"] == "not_deleted"
            ]
            cursor = response["data"]["viewer"]["availableBotsConnection"]["pageInfo"][
                "endCursor"
            ]
            bots += new_bots
            if len(new_bots) == 0:
                if not get_all:
                    print(f"Only {len(bots)} bots found on this account")
                else:
                    print("Succeed to get all available bots")
                self.bots.update({bot["handle"]: {"bot": bot} for bot in bots})
                return self.bots
            
        print("Succeed to get available bots")
        self.bots.update({bot["handle"]: {"bot": bot} for bot in bots})
        return self.bots
     
    def get_chat_history(self, bot:str=None, handle:str="", useBot:bool=False): 
        variables = {'handle': handle, 'useBot': useBot}
        response_json = self.send_request('gql_POST', 'ChatsHistoryPageQuery', variables)
        edges = response_json['data']['chats']['edges']
        
        chat_bots = {}
        
        if bot == None:
            print('-'*18+' \033[38;5;121mChat History\033[0m '+'-'*18)
            print('\033[38;5;121mChat ID\033[0m  |     \033[38;5;121mChat Code\033[0m       | \033[38;5;121mBot Name\033[0m')
            print('-' * 50)
            for edge in edges:
                chat = edge['node']
                model = bot_map(chat["defaultBotObject"]["displayName"])
                print(f'{chat["chatId"]} | {chat["chatCode"]} | {model}')
                if model in chat_bots:
                    chat_bots[model].append({"chatId": chat["chatId"],"chatCode": chat["chatCode"], "id": chat["id"]})
                else:
                    chat_bots[model] = [{"chatId": chat["chatId"], "chatCode": chat["chatCode"], "id": chat["id"]}]
            print('-' * 50)
        else:
            for edge in edges:
                chat = edge['node']
                try:
                    model = bot_map(chat["defaultBotObject"]["displayName"])
                    if model == bot:
                        if model in chat_bots:
                            chat_bots[model].append({"chatId": chat["chatId"],"chatCode": chat["chatCode"], "id": chat["id"]})
                        else:
                            chat_bots[model] = [{"chatId": chat["chatId"], "chatCode": chat["chatCode"], "id": chat["id"]}]
                except:
                    pass           
        return chat_bots
    
    def create_new_chat(self, bot: str="a2", message: str=""):
        variables = {"bot":bot,"query":message,"source":{"sourceType":"chat_input","chatInputMetadata":{"useVoiceRecord":False,"newChatContext":"chat_settings_new_chat_button"}},"sdid":"","attachments":[]}
        response_json = self.send_request('gql_POST', 'ChatHelpersSendNewChatMessageMutation', variables)
        if response_json["data"] is None and response_json["errors"]:
            raise ValueError(
                f"Bot {bot} not found. Make sure the bot exists before creating new chat."
            )
        chatCode = response_json['data']['messageEdgeCreate']['chat']['chatCode']
        print(f'New Thread created | {chatCode}')
        return chatCode

    def send_message(self, bot: str, message: str, chatId: int=None, chatCode: str=None):
        if (chatId == None and chatCode == None):
            chatCode = self.create_new_chat(bot, message)
        else:
            chat_data = self.get_chat_history(bot=bot)[bot]
            for chat in chat_data:
                if chat['chatId'] == chatId and chatCode == None:
                    chatCode = chat['chatCode']
                    break
                if chat['chatCode'] == chatCode and chatId == None:  
                    chatId = chat['chatId']
                    break    
            variables = {'bot': bot, 'chatId': chatId, 'query': message, 'source': { "sourceType": "chat_input", "chatInputMetadata": {"useVoiceRecord": False}}, 'withChatBreak': False, "clientNonce": generate_nonce(), 'sdid':"", 'attachments': []}
            self.send_request('gql_POST', 'SendMessageMutation', variables)
        return self.get_latest_message(chatCode)
        
    def chat_break(self, bot: str, chatId: int=None, chatCode: str=None):
            chat_data = self.get_chat_history(bot=bot)[bot]
            for chat in chat_data:
                if chat['chatId'] == chatId or chat['chatCode'] == chatCode:
                    chatId = chat['chatId']
                    id = chat['id']
                    break
            variables = {"connections": [
                    f"client:{id}:__ChatMessagesView_chat_messagesConnection_connection"],
                    "chatId": chatId}
            self.send_request('gql_POST', 'ChatHelpers_addMessageBreakEdgeMutation_Mutation', variables)
        
    def delete_message(self, message_ids):
        variables = {'messageIds': message_ids}
        self.send_request('gql_POST', 'DeleteMessageMutation', variables)
    
    def purge_conversation(self, bot: str, chatId: int=None, chatCode: str=None, count: int=50):
        if chatId != None and chatCode == None:
            chatdata = self.get_chat_history(bot=bot)[bot]
            for chat in chatdata:
                if chat['chatId'] == chatId:
                    chatCode = chat['chatCode']
                    break
        variables = {'chatCode': chatCode}
        response_json = self.send_request('gql_POST', 'ChatPageQuery', variables)
        edges = response_json['data']['chatOfCode']['messagesConnection']['edges']
        
        num = count
        while True:
            if len(edges) == 0 or num == 0:
                break
            message_ids = []
            for edge in edges:
                message_ids.append(edge['node']['messageId'])
            self.delete_message(message_ids)
            num -= len(message_ids)
            if len(edges) < num:
                response_json = self.send_request('gql_POST', 'ChatPageQuery', variables)
                edges = response_json['data']['chatOfCode']['messagesConnection']['edges']
                
        print(f"Deleted {count-num} messages")
            
    def purge_all_conversations(self):
        self.send_request('gql_POST', 'DeleteUserMessagesMutation', {})
        
    def get_latest_message(self, chatCode: str=""):
        variables = {'chatCode': chatCode}
        state = 'incomplete'
        while True:
            sleep(0.1)
            response_json = self.send_request('gql_POST','ChatPageQuery', variables)
            edges = response_json['data']['chatOfCode']['messagesConnection']['edges']
            chatId = response_json['data']['chatOfCode']['chatId']
            if edges:
                latest_message = edges[-1]['node']
                text = latest_message['text']
                state = latest_message['state']
                if state == 'complete':
                    break
            else:
                text = 'Fail to get a message. Please try again!'
                break
        return {"response": text, "chatId": chatId, "chatCode": chatCode}
    
    def delete_chat(self, bot: str, chatId: any=None, chatCode: any=None, del_all: bool=False):
        chatdata = self.get_chat_history(bot=bot)[bot]
        if chatId != None and not isinstance(chatId, list):
            self.send_request('gql_POST', 'DeleteChat', {'chatId': chatId})
            print(f'Chat {chatId} deleted') 
        if del_all == True:
            for chat in chatdata:
                self.send_request('gql_POST', 'DeleteChat', {'chatId': chat['chatId']})
                print(f'Chat {chat["chatId"]} deleted')
        if chatCode != None:
                for chat in chatdata:
                    if isinstance(chatCode, list):
                        if chat['chatCode'] in chatCode:
                            chatId = chat['chatId']
                            self.send_request('gql_POST', 'DeleteChat', {'chatId': chatId})
                            print(f'Chat {chatId} deleted')
                    else:
                        if chat['chatCode'] == chatCode:
                            chatId = chat['chatId']
                            self.send_request('gql_POST', 'DeleteChat', {'chatId': chatId})
                            print(f'Chat {chatId} deleted')
                            break               
        elif chatId != None and isinstance(chatId, list):
            for chat in chatId:
                self.send_request('gql_POST', 'DeleteChat', {'chatId': chat})
                print(f'Chat {chat} deleted')   
        
    def complete_profile(self, handle: str=None):
        if handle == None:
            handle = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(10))
        variables = {"handle" : handle}
        self.send_request('gql_POST', 'NuxInitialModal_poeSetHandle_Mutation', variables)
        self.send_request('gql_POST', 'MarkMultiplayerNuxCompleted', {})
    
    def create_bot(self, handle, prompt, display_name=None, base_model="chinchilla", description="", intro_message="", api_key=None, api_bot=False, api_url=None, prompt_public=True, pfp_url=None, linkification=False,  markdown_rendering=True, suggested_replies=False, private=False, temperature=None):
        # Auto complete profile
        try:
            self.send_request('gql_POST', 'MarkMultiplayerNuxCompleted', {})
        except:
            self.complete_profile()
        variables = {
            "model": base_model,
            "displayName": display_name,
            "handle": handle,
            "prompt": prompt,
            "isPromptPublic": prompt_public,
            "introduction": intro_message,
            "description": description,
            "profilePictureUrl": pfp_url,
            "apiUrl": api_url,
            "apiKey": api_key,
            "isApiBot": api_bot,
            "hasLinkification": linkification,
            "hasMarkdownRendering": markdown_rendering,
            "hasSuggestedReplies": suggested_replies,
            "isPrivateBot": private,
            "temperature": temperature
        }
        result = self.send_request('gql_POST', 'PoeBotCreate', variables)['data']['poeBotCreate']
        if result["status"] != "success":
           print(f"Poe returned an error while trying to create a bot: {result['status']}")
        else:
           print("Bot created successfully")
        
    # get_bot logic 
    def get_botData(self, handle):
        variables = {"botHandle": handle}
        try:
            response_json = self.send_request('gql_POST', 'BotLandingPageQuery', variables)
            return response_json['data']['bot']
        except Exception as e:
            raise ValueError(
                f"Fail to get botId from {handle}. Make sure the bot exists and you have access to it."
            ) from e

    def edit_bot(self, handle, prompt, display_name=None, base_model="chinchilla", description="",
                intro_message="", api_key=None, api_url=None, private=False,
                prompt_public=True, pfp_url=None, linkification=False,
                markdown_rendering=True, suggested_replies=False, temperature=None):     
        variables = {
        "baseBot": base_model,
        "botId": self.get_botData(handle)['botId'],
        "handle": handle,
        "displayName": display_name,
        "prompt": prompt,
        "isPromptPublic": prompt_public,
        "introduction": intro_message,
        "description": description,
        "profilePictureUrl": pfp_url,
        "apiUrl": api_url,
        "apiKey": api_key,
        "hasLinkification": linkification,
        "hasMarkdownRendering": markdown_rendering,
        "hasSuggestedReplies": suggested_replies,
        "isPrivateBot": private,
        "temperature": temperature
        }
        result = self.send_request('gql_POST', 'PoeBotEdit', variables)["data"]["poeBotEdit"]
        if result["status"] != "success":
             print(f"Poe returned an error while trying to edit a bot: {result['status']}")
        else:
             print("Bot edited successfully")
      
    def delete_bot(self, handle):
        isCreator = self.get_botData(handle)['viewerIsCreator']
        botId = self.get_botData(handle)['botId']
        try:
            if isCreator == True:
                response = self.send_request('gql_POST', "BotInfoCardActionBar_poeBotDelete_Mutation", {"botId": botId})
            else:
                response = self.send_request('gql_POST',
                    "BotInfoCardActionBar_poeRemoveBotFromUserList_Mutation",
                    {"connections": [
                        "client:Vmlld2VyOjA=:__HomeBotSelector_viewer_availableBotsConnection_connection"],
                        "botId": botId}
                )
        except Exception:
            raise ValueError(
                f"Failed to delete bot {handle}. Make sure the bot exists and belongs to you."
            )
        if response["data"] is None and response["errors"]:
            raise ValueError(
                f"Failed to delete bot {handle} :{response['errors'][0]['message']}"
            )
        else:
            print("Bot deleted successfully")