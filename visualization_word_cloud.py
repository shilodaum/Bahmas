import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from os import path
from PIL import Image

# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
text = """
Featured article
1860 Boden Professor of Sanskrit election
From Wikipedia, the free encyclopedia
Jump to navigation
Jump to search
Monier Williams, elected as the second Boden Professor of Sanskrit in 1860; this photograph was taken by Lewis Carroll.

The election in 1860 for the position of Boden Professor of Sanskrit at the University of Oxford was a competition between two candidates offering different approaches to Sanskrit scholarship. One was Monier Williams, an Oxford-educated Englishman who had spent 14 years teaching Sanskrit to those preparing to work in British India for the East India Company. The other, Max Müller, was a German-born lecturer at Oxford specialising in comparative philology, the science of language. He had spent many years working on an edition of the Rig Veda (an ancient collection of Vedic Sanskrit hymns) and had gained an international reputation for his scholarship. Williams, in contrast, worked on later material and had little time for the "continental" school of Sanskrit scholarship that Müller exemplified. Williams regarded the study of Sanskrit as a means to an end, namely the conversion of India to Christianity. In Müller’s opinion, his own work, while it would assist missionaries, was also valuable as an end in itself.

The election came at a time of public debate about Britain's role in India in the wake of the Indian Rebellion of 1857. Opinions were divided on whether greater efforts should be made to convert India or whether to remain sensitive to local culture and traditions. Both men battled for the votes of the electorate (the Convocation of the university, consisting of over 3,700 graduates) through manifestos and newspaper correspondence. Williams laid great stress in his campaign on the intention of the original founder of the chair, that the holder should assist in converting India through dissemination of the Christian scriptures. Müller's view was that his work on the Rig Veda was of great value for missionary work, and published testimonials accordingly. He also wanted to teach wider subjects such as Indian history and literature to assist missionaries, scholars, and civil servants – a proposal that Williams criticised as not in accordance with the original benefactor's wishes. The rival campaigns took out newspaper advertisements and circulated manifestos, and different newspapers backed each man. Although generally regarded as superior to Williams in scholarship, Müller had the double disadvantage (in the eyes of some) of being German and having liberal Christian views. Some of the newspaper pronouncements in favour of Williams were based on a claimed national interest of having an Englishman as Boden professor to assist with the work of governing and converting India.

Special trains to Oxford were provided on the day of the election, 7 December 1860, for non-resident members of Convocation to cast their votes. At the end of the hard-fought campaign, Williams won by a majority of over 220 votes. Thereafter, he helped to establish the Indian Institute at Oxford, received a knighthood, and held the chair until his death in 1899. Müller, although deeply disappointed by his defeat, remained in Oxford for the rest of his career, but never taught Sanskrit there. The 1860 election was the last time that Convocation chose the Boden professor, as this power was removed in 1882 as a result of reforms imposed by Parliament. As of 2017, the professorship is still in existence, and is now the last remaining Sanskrit professorship in the United Kingdom.
Contents

    1 Background
    2 Candidates
        2.1 Müller's manifesto
        2.2 Williams's manifesto
    3 Rival campaigns
    4 Supporters and newspapers
    5 Election
    6 Subsequent events
    7 Notes
    8 References
        8.1 Bibliography

Background
Main article: Boden Professor of Sanskrit
Further information: Company rule in India and British Raj

The position of Boden professor at the University of Oxford was established by the bequest of Lieutenant Colonel Joseph Boden of the Bombay Native Infantry, who died in 1811. His will provided that on the death of his daughter (which occurred in 1827), his estate should pass to the university to fund a Sanskrit professorship. His purpose was to convert the people of India[n 1] to Christianity "by disseminating a knowledge of the Sacred scriptures among them".[2] The university statutes governing the chair provided that the professor should be chosen by the members of Convocation – all those who had obtained the Oxford degree of Master of Arts, whether or not they taught in the university – rather than by the professors and college fellows.[3] At the time of the 1860 election, there were 3,786 members of Convocation.[4] According to the religious historian Gwilym Beckerlegge, the professorship was regarded at the time as "prestigious and handsomely remunerated".[1] An editorial in the British national newspaper The Times in 1860 said that the professorship was "one of the most important, most influential, and most widely known institutions at Oxford, not to say in the whole civilised world."[5] It paid between £900 and £1,000 per year for life.[6]

The first Boden professor, Horace Hayman Wilson, was elected in 1832 and died on 8 May 1860.[7] The election for his successor came at a time of public debate about the nature of British missionary work in India, particularly after the Indian Rebellion of 1857. The East India Company, which controlled the British territories until they were absorbed into the British Empire in 1858, had had a general policy until 1813 of non-interference with Indian customs, including religion. Christian missionaries required a licence to proselytize. In practice, most could operate without a licence, except for Evangelicals, who were regarded as too radical in an age when Christians from other backgrounds were more prepared to be tolerant of other faiths. As the Evangelical movement grew in strength, it pressed for greater efforts to bring Christianity to India, and so the company relaxed its approach to missionaries in 1813.[8] After 1858, the British government was reluctant to provoke further unrest by interference with local traditions and religion, but many of those charged with running India were themselves Evangelicals sympathetic to efforts to convert the country. As Beckerlegge has commented, "the furtherance of Christian mission had become inextricably bound up with attempts to define Britain's role in India and indeed to justify Britain's presence in India."[9] The issue was whether Britain was there simply to govern India or to "civilise" it, and if the latter, whether to draw up or destroy India's existing culture and religion.[10] Many of those who supported increased missionary work in India, says Beckerlegge, regarded the events of 1857 as "nothing less than a divine judgment" on Britain's failure to bring Christianity to the country.[11]

There were two schools of thought on whether Sanskrit should be taught for the purpose of assisting the administration and conversion of India, or for its own merits. The East India Company had provided instruction in Sanskrit to its employees at its college at Haileybury, Hertfordshire, and the College of Fort William in Calcutta, to educate them in local culture. For some, this led to an interest in Indian religion and culture as revealed in the Sanskrit texts. This was in contrast to the situation in continental Europe, where scholars examined Sanskrit as part of the "science of language", comparative philology, rather than for reasons of imperial administration. Fewer European scholars visited India, but many British Sanskritists had lived and worked there.[12] Some British scholars in other fields had strong doubts in any event about Sanskrit, as a "crude linguistic forgery pieced out of Latin and Greek", or as proving little "except a thoroughly unwelcome kinship between Briton and Brahmin", in the words of the American academic Linda Dowling.[13]
Candidates
Max Müller, photographed in 1857 by Lewis Carroll

Although five men indicated their intent to seek the chair in 1860 or were proposed in their absence, in the end the two who contested the election were Monier Williams and Max Müller. Williams (known later in life as Sir Monier Monier-Williams) was the son of an army officer and was born in India. He studied briefly at Balliol College, Oxford, before training at Haileybury for the civil service in India. The death of his brother in battle in India led to him to return to Oxford to complete his degree. He also studied Sanskrit with Wilson before teaching this and other languages at Haileybury from 1844 until 1858, when it closed following the Indian rebellion.[14] He prepared an English–Sanskrit dictionary, at Wilson's prompting, which the East India Company published in 1851; his Sanskrit–English dictionary was supported by the Secretary of State for India.[15] As the Dutch anthropologist Peter van der Veer has written, Williams "had an Evangelical zeal" in line with the views that had inspired Boden to establish the chair.[16]

Müller was from the German duchy of Anhalt-Dessau and took up Sanskrit at university as a fresh intellectual challenge after mastering Greek and Latin.[17] At this time, Sanskrit was a comparatively new subject of study in Europe, and its connections with the traditional classical languages had attracted interest from those examining the nature and history of languages.[18] He obtained his doctorate from Leipzig University in 1843, aged 19, and after a year studying in Berlin he began work in Paris on the first printed edition of the Rig Veda (an ancient collection of Vedic Sanskrit hymns). What was supposed to be a brief visit to England for research in 1846 turned into a lifelong stay. The Prussian diplomat Baron von Bunsen and Wilson persuaded the directors of the East India Company to provide financial support for Oxford University Press to publish the Rig Veda. Müller settled in Oxford in 1848 and continued his Sanskrit research, becoming Taylorian Professor of Modern European Languages in 1854 after three years as the deputy professor;[17] in this post he was paid £500 per year, half the stipend of the Boden chair.[19] A British subject from 1855, he was elected a fellow of All Souls College in 1858,[17] "an unprecedented honour for a foreigner at that time", in the words of his biographer, the Indian writer Nirad C. Chaudhuri.[20]

Three other scholars indicated an intention to stand for the chair, or were nominated by others, but withdrew before the ballot. The candidacy of Edward Cowell, Professor of Sanskrit at the Government College in Calcutta, was announced in The Times on 28 May 1860, where it was said that Wilson had pronounced him "eminently qualified" to succeed him.[21] He later wrote from India refusing to stand against Müller.[22] Ralph Griffith, a former Boden scholar who was a professor at the Government Sanskrit College in Benares, announced his candidacy in August 1860, but withdrew in November.[23][24] James R. Ballantyne, principal of the college in Benares, was proposed in June 1860 by friends based in England, who described him as the "chief of British Sanscrit scholars".[25]
Müller's manifesto
	Wikisource has original text related to this article:
Max Müller's election submission

Müller announced his candidacy on 14 May 1860, six days after Wilson's death.[26] His submission to Convocation referred to his work in editing the Rig Veda, saying that without it missionaries could not fully learn about the teachings of Hinduism, which impeded their work. He therefore considered that he had "spent the principal part of my life in promoting the object of the Founder of the Chair of Sanskrit."[27] He promised to work exclusively on Sanskrit, and said that he would provide testimonials from "the most eminent Sanskrit scholars in Europe and India" and from missionaries who had used his publications to help "overthrow the ancient systems of idolatry" in India.[27] In due course, he was able to provide a list of missionary societies that had requested copies of the Rig Veda from the East India Company, including the Church Missionary Society and the Society for the Propagation of the Gospel.[28]
Williams's manifesto
	Wikisource has original text related to this article:
Monier Williams's election submission

Williams declared his intention to stand for election on 15 May 1860, one day after Müller.[29] In his written submission to Convocation, he emphasised his suitability for appointment in the light of Boden's missionary wishes. After giving details of his life and career, particularly his experience in Sanskrit obtained at Haileybury, he stated that for the past 14 years "the one idea of my life has been to make myself thoroughly conversant with Sanskrit, and by every means in my power to facilitate the study of its literature."[30] He assured voters that, if elected, "my utmost energies shall be devoted to the one object which its Founder had in view;—namely 'The promotion of a more general and critical knowledge of the Sanskrit language, as a means of enabling Englishmen to proceed in the conversion of the natives of India to the Christian religion.'"[30] Unlike Müller, he regarded the study of Sanskrit "as chiefly a means to the missionary conversion of the Hindus rather than as an end in itself", as Dowling puts it.[13] In this way, Dowling says, he could attempt to deflect attention from his "modest abilities in classical Sanskrit" when compared to Müller's "internationally acknowledged achievements".[13] Moreover, the appeal to Boden's original intentions came during a period when Convocation tended to pay little attention to the expressed wishes of benefactors.[31]
Rival campaigns
Part of a handbill issued by supporters of Williams on 30 November 1860

    There are Two Candidates, with ample Testimonials.
    The Organs of Public Opinion have thought the contest not unworthy of their notice.
    What then is the result?
    By common consent both are pronounced scholars of world-wide reputation.
    But one of them is specially and earnestly recommended to Convocation by a great number of our Countrymen in India itself.
    These Englishmen, educated by him, grateful for his instruction, and personally attached to him, are a machinery existing ready to hand for the great work to be done.
    They have no Votes to give, but their voice from that distant land should ring in our ears and hearts.
    They know their man, they know the Natives, they are in daily communication with them. Is it wise to disregard their opinion?
    The Professorship is not for Oxford alone.
    It is not for 'The Continent and America'.
    It is for India.
    It is for Christianity.
    Let us then Vote for the man who is well-known and loved in India, and who, even by the voice of his opponents, is declared to be a trustworthy depositary of the Christian interests of a Christian Foundation.
          M.A.[31][32]

In August 1860, Müller wrote to the members of Convocation about his plans to teach a broad range of topics in addition to Sanskrit, including comparative philology, Indian history, and literature. Simply teaching the language "would be but a mean return" for Boden's generosity, he wrote.[33] In this way, he would help to supply "efficient" missionaries, "useful" civil servants, and "distinguished" Boden scholars.[34]

In turn, Williams wrote that if Boden had left instructions that the man elected should be the one "most likely to secure a world-wide reputation for the Sanskrit Chair, I confess that I should have hesitated to prosecute my design."[35] However, this was not the case and it would be "unjustifiable" in terms of the statutes governing the chair if the professor were to lecture on wider topics. In his view, the Vedic literature was "of less importance" and the philosophical literature was "very mystical and abstruse", whereas "the classical or modern" period (the laws, two heroic poems, and the plays) was the "most important".[36] Reminding his readers that he had edited two Sanskrit plays, he stated that the literature of the third period constituted the Sanskrit scriptures, not ("as has hitherto been believed") the Veda, "still less the Rig Veda".[36] He commented that Müller's edition of the Rig Veda was requiring "an expenditure of time, labour, money, and erudition far greater than was ever bestowed on any edition of the Holy Bible", adding that Boden did not intend to "aid in the missionary work by perpetuating and diffusing the obsolescent Vedic Scriptures."[36] He claimed that his own approach to Sanskrit scholarship, with his dictionaries and grammar books, was "suited to English minds", unlike Müller's "continental" and "philosophical" approach, which dealt with texts no longer relevant to modern Hindus that missionaries would not benefit from studying.[34]

In a letter to The Times published on 29 October 1860, Müller took issue with Williams. To the claim that it would be unjustifiable to teach history, philosophy, and other subjects as Boden professor, he quoted from one of Wilson's public lectures in which he had said that it had always been his intention to offer "a general view of the institutions and social condition, the literature, and religion of the Hindus."[37] He noted that he had published in all three areas into which Williams divided Sanskrit literature, and disputed Williams's views on the relative importance of Vedic literature with reference to a review of one of his publications by Wilson. Williams, he said, "stands as yet alone" in asserting that the heroic poems and the plays, not the Vedas, were the real scriptures.[37] He refused to accept Williams's estimate of the labour involved in the edition of the Rig Veda, and said that to compare his little effort with that carried out on the Bible was "almost irreverent".[37] He concluded by attempting to rebut the claim that Boden would not have wanted the Vedic scriptures to be supported. He noted that the Bishop of Calcutta (George Cotton) had written that it was of "the greatest importance" for missionaries to study Sanskrit and its scriptures "to be able to meet the Pundits on their own ground", and that the bishop's view was that nothing could be more valuable in this work than Müller's edition, and Wilson's translation, of the Rig-Veda."[37][n 2]

After this letter, Williams complained about Müller conducting his campaign in the newspapers and misrepresenting what Williams was saying.[10] Müller asked three professors and the Provost of Queen's College to consider the accuracy of his letter, and they pronounced in his favour.[38] In Beckerlegge's view, all these replies and counter-replies did was "illustrate the increasingly heated tone of the exchanges" between the two men and their supporters.[10] It was "as if the protagonists were prospective members of Parliament", in the words of one modern scholar.[4] Terence Thomas, a British lecturer in religious studies, records "insults regarding the nationality of Max Müller and the proficiency of Monier Williams as a Sanskritist being bandied back and forth by their supporters."[39] For example, one of the Boden scholars at Oxford, Robinson Ellis, claimed that Williams had not been able to prove that he could read a Sanskrit text. When challenged, he later amended this to a claim that Williams could only read a text when he could compare it to another one, describing this as "mechanical labour which is paid for at the public libraries at Paris and Berlin at the rate of half a crown a year."[40]

Each had a committee of helpers; Williams had two, one in London, the other in Oxford.[41] He spent over £1,000 on his campaign – as much as the Boden professor was paid in a year.[4] In June 1860, Müller complained in a letter to his mother about having to write to each one of the "4,000 electors, scattered all over England"; he said that sometimes he wished he had not thought of standing for election, adding "if I don't win, I shall be very cross!".[42]
Supporters and newspapers
Letter from Wilson to Williams, 21 April 1860

    My dear Williams, I am quite incompetent to give you any hints for your industry, for I have been and am suffering dreadfully. I am about to undergo an operation; and, as there is always a certain amount of risk in such an operation at my age, I recommend your being alive to the chance of a vacancy. I have always looked to you as my successor; but you will have a formidable competitor in M. Müller, not only for his celebrity, but personal influence. However, if God be pleased, I may get over the trial, and for a few years more keep you in expectancy.
      Yours ever affectionately,
         H. H. Wilson[43]

According to Beckerlegge, there was a view held by many of those involved in the keenly fought struggle between Williams and Müller that more depended on the result than simply one man's career – missionary success or failure in India, "and even the future stability of British rule in this region" (in the light of events in India a few years previously) might depend on the abilities of the Boden professor.[1] Victory would depend on each side's ability to persuade non-resident members of Convocation to return to Oxford to cast their votes.[3] Each candidate had their supporters: Müller was backed by scholars of international merit, whereas Williams was able to call upon Oxford-based academics and those who had served in India as administrators or missionaries.[3] Both candidates claimed support from Wilson – "as if the principle of apostolic succession was involved in the appointment", says Chaudhuri.[43] The Times reported on 23 May that friends of Williams placed considerable weight upon a private letter to him from Wilson, "indicating Mr. Williams as his probable successor."[44] In return, Wilson was revealed to have said "two months before his death" that "Mr. Max Müller was the first Sanskrit scholar in Europe".[44] The source of this information was W. S. W. Vaux, of the British Museum, who described his conversation with Wilson in a letter to Müller in May 1860. In reply to Vaux's comment that he and others wanted Wilson's successor to be "the finest man we could procure", Vaux quoted Wilson as saying that "You will be quite right if your choice should fall on Max Müller."[45]

The Times published a list of leading supporters for each candidate on 27 June 1860, noting that many people were not declaring support for either "since they wish to see whether any person of real eminence announces himself from India".[46] Müller was backed by Francis Leighton, Henry Liddell and William Thomson (the heads of the colleges of All Souls, Christ Church, and Queen's), Edward Pusey, William Jacobson and Henry Acland (the Regius Professors of Hebrew, of Divinity, and of Medicine) and others. Williams had the declared support of the heads of University and Balliol colleges (Frederick Charles Plumptre and Robert Scott), and fellows from ten different colleges.[46]
Müller's supporters included Samuel Wilberforce, Bishop of Oxford in 1860 and later Bishop of Winchester.

On 5 December 1860, two days before the election, friends of Müller took out an advertisement in The Times to list his supporters, in response to a similar record circulated on behalf of Williams. By then, Müller's list included the heads of 11 colleges or halls of the university, 27 professors, over 40 college fellows and tutors, and many non-resident members of the university including Samuel Wilberforce (the Bishop of Oxford) and Sir Charles Wood (the Secretary of State for India).[47] A list published on the following day added the name of Charles Longley, Archbishop of York, to Müller's supporters.[48] Overall, the public supporters for each candidate were about the same in number, but while Müller was backed by "all the noted Orientalists of Europe of the age", Williams's supporters "were not so distinguished", according to Chaudhuri.[6][41][n 3]

Newspapers and journals joined the debate, some in strong terms. One evangelical publication, The Record, contrasted the two candidates: Müller's writings were "familiar to all persons interested in literature, while they have destroyed confidence in his religious opinions"; Williams was described as "a man of sincere piety, and one who is likely, by the blessing of God on his labours, to promote the ultimate object which the founder of the Professorship had in view."[50] Other newspapers highlighted the nationalities of the candidates; as Beckerlegge has put it, "voting for the Boden Chair was increasingly taking on the appearance of being a test of patriotism."[51] The Homeward Mail (a London-based newspaper that concentrated on news from, and relating to, India)[52] asked its readers whether they wanted "a stranger and a foreigner" to win, or "one of your own body".[50] A writer in The Morning Post said that voters should "keep the great prizes of the English universities for English students".[50] The Morning Herald said that it was "a question of national interest", since it would affect the education of civil servants and missionaries and therefore "the progress of Christianity in India and the maintenance of British authority in that empire".[50] It anticipated that Britain would be ridiculed if it had to appoint a German to its leading academic Sanskrit position.[50]

Müller was not without support in the press. An editorial in The Times on 29 October 1860 called him "nothing more nor less than the best Sanscrit scholar in the world."[5] It compared the situation to the 1832 election, when there had also been a choice between the best scholar (Wilson) and a good scholar "who was held to have made the most Christian use of the gift" (William Hodge Mill).[5] Williams, it said, appeared as "the University man ... , the man sufficiently qualified for the post, and, above all, as the man in whose hands, it is whispered, the interests of Christianity will be perfectly safe."[5] His proposal not to teach history, philosophy, mythology or comparative philology "seems to strip the subject very bare" and would, it thought, leave the post as "an empty chair".[5] It stated that Müller "best answers to the terms of Colonel Boden's foundation."[5] His field of study – the oldest period of Sanskrit literature – "must be the key of the whole position", whereas Williams was only familiar with the later, "less authentic, and less sacred" writings.[5] The editorial ended by saying that Oxford "will not choose the less learned candidate; at all events, it will not accept from him that this is the true principle of a sound Christian election."[5]

Pusey, the influential "high church" Anglican theologian associated with the Oxford Movement, wrote a letter of support to Müller, reproduced in The Times. In his view, Boden's intentions would be best advanced by electing Müller. Missionaries could not win converts without knowing the details of the religion of those with whom they were dealing, he wrote, and Müller's publications were "the greatest gifts which have yet been bestowed" on those in such work.[53] He added that Oxford would gain by electing him to a position where Müller could spend all his time on work "of such primary and lasting importance for the conversion of India."[53] Beckerlegge finds Pusey's support noteworthy, since Pusey would not have agreed with Müller's particular "broad" approach to Christianity, and was thus providing a judgment on the academic abilities of the candidate best placed to advance missionary work in India.[28] One anonymous writer of a letter to the press in support of Müller, shortly before the election, expressed it thus: "A man's personal character must stand very high, and his theological opinions can afford but little ground for animadversion on either hand, when he unites as his unhesitating supporters Dr. Pusey and Dr. Macbride"[54] – a reference to John Macbride, described in the Oxford Dictionary of National Biography as "a profoundly religious layman of the 'old' evangelical school".[55] However, Dowling describes Müller as "impercipient of the subtle twists of theological argument, the fine shadings and compunctions of Victorian religious feeling" – a weakness that was held against him.[56]
Election
The Times, 8 December 1860

    In a Convocation held in the Sheldonian Theatre at 2 o'clock an election was held of a Boden Sanskrit Professor, to replace the late Mr H. H. Wilson. There were two candidates, Mr. Monier Williams, M.A., of University College, late Professor of Sanskrit at Haileybury, and Mr. Max Müller, M.A., of Christ Church and All Souls' Colleges, Taylorian Professor of Modern European Languages in the University of Oxford. Mr Williams took the lead from the first, and, as hour after hour went by, continually increased his majority. The poll was closed at about half-past 7, and the Senior Proctor declared Mr. Williams duly elected to the office. We understand that the numbers at the close were:
         For Mr. Williams 833
         For Professor Müller 610
         Majority 223.[57]

The election was held on 7 December 1860 in the Sheldonian Theatre.[57] Three special trains were laid on between Didcot and Oxford that afternoon to meet passengers travelling from the west of England, and one additional train was provided between Oxford and London via Didcot in the evening. A London-bound train from the north of England called additionally at Bletchley to allow onward connections to Oxford for passengers from places such as Liverpool, Manchester and Birkenhead.[48] Evangelical clergymen turned out in force to vote.[40] Over about five and a half hours of voting, 833 members of Congregation declared for Williams, 610 for Müller.[57]

Historians have advanced various views as to why, even though Müller was generally regarded as the superior scholar, he lost to Williams.[58] Beckerlegge suggests several possible factors: unlike Williams, Müller was known as a writer and translator rather than a teacher of Sanskrit, he did not have links to the East India Company or the Indian Civil Service that he could call upon for supporters, and he had not been educated at Oxford.[59] In his obituary of Müller, Arthur Macdonell (Boden professor 1899–1926) said that the election "came to turn on the political and religious opinions of the candidates rather than on their merits as Sanskrit scholars", adding that "party feeling ran high and large numbers came up to vote."[60] Similarly, Dowling has written that "in the less cosmopolitan precincts outside Oxford ... the argument that Müller was 'not English' told heavily against him" since "the argument was (and was meant to be, of course) unanswerable."[56] She adds that Tories opposed him for his liberal political views, traditionalist factions within Oxford rejected "Germanizing" reform, and "the Anglican clergy ... detected unbelief lurking in his umlaut".[56] The American historian Marjorie Wheeler-Barclay takes the view that the three motives for people voting against Müller cannot be disentangled.[61] Those who supported Indian missionary work, Dowling writes, saw it as the key to continued British rule, and there was no need to take a chance by electing Müller, who had "a reputation for unsound religious opinions", since Williams was a scholar "of distinction known for his conservatism and piety."[62]

Müller attributed his defeat to his German background and suspicions that his Christianity was insufficiently orthodox, factors that had been used to influence in particular those voters who were no longer resident members of the university.[59] He had lost, he wrote, because of "calumnious falsehood and vulgar electioneering tactics."[56] Williams wrote in his unpublished autobiography that he had been "favoured by circumstances" and that, unlike Müller, he had been regarded as politically and religiously conservative.[59]
Subsequent events
Müller writes to his mother, 16 December

    The last days have been full of disturbance. You will have seen by the papers that I did not get the Sanskrit Professorship. The opposite party made it a political and religious question, and nothing could be done against them. All the best people voted for me, the Professors almost unanimously, but the vulgus profanum made the majority. I was sorry, for I would gladly have devoted all my time to Sanskrit, and the income was higher; but we shall manage.[63]

Williams served as Boden professor until his death in 1899, although he retired from teaching (while retaining the title) in 1887 because of his health.[14] He took as the title for his inaugural lecture "The Study of Sanskrit in Relation to Missionary Work", in keeping with his views as to the role of the chair. Thomas notes that as the East India Company had switched to using English rather than Sanskrit or Persian for its work, "a natural source of students had already dried up not long after the Boden Chair was inaugurated [in 1832]".[64] Williams helped establish the Indian Institute at Oxford, proposing the idea in 1875 and helping to raise funds for the project on his visits to India, and persuaded the university to add a degree course in oriental studies. His publications included translations of plays and grammatical works. He received a knighthood in 1886, and was appointed a Knight Commander of the Order of the Indian Empire in 1887, when he changed his surname to become Sir Monier Monier-Williams.[14]

Robinson Ellis was required to attend Williams's lectures despite his low opinions of the new professor's abilities. Williams said that Ellis's "whole demeanour was that of a person who would have welcomed an earthquake or any convulsion of nature which would have opened a way for him to sink out of my sight".[40] Overall, Williams won over most of those who had opposed his election, with the exception of Müller.[40]

For Müller, losing the election was "a decisive turning point in his scholarly and intellectual life", according to Chaudhuri.[20] It meant that Müller was never to teach Sanskrit at Oxford, although he remained there until his death in 1900;[15] nor did he ever visit India.[12] Greatly disappointed by not winning the chair, Müller "regularly avoided or snubbed Monier Williams and his family on the streets of Oxford", according to Williams.[65] He was appointed to a chair of comparative philology in 1868, the first Oxford professorship to be established by the university itself without money from royal or private donations.[58] He wrote a letter of resignation in 1875 when the university proposed to award an honorary doctorate to Williams, giving as his reason that he wanted to spend more time studying Sanskrit. Friends attempted to talk him out of it, and the university then appointed a deputy professor to discharge his duties, an honour he greatly appreciated.[66]

The Indian historian Rajesh Kochhar, noting the East India Company's support for Müller, commented that "Oxford professors may have had their own reasons for their assessment of him, but the Company and the natives both found him very relevant."[15] Despite his electoral defeat, he enjoyed a high reputation at Oxford and beyond: he "occupied a central role in the intellectual life of the nation", according to Beckerlegge,[67] and was "viewed by the world as a model of academic success" (as Dowling puts it).[68] Dowling considers that "[w]ithin his own lifetime, Müller was discredited as a linguistic scientist" and has "little relevance" to later models of the study of language.[68] In Beckerlegge's opinion, Müller's views about the nature of Christian missionary work showed the difficulty at that time for Christian academics "actively working to promote a more tolerant and even-handed study of other religious traditions".[69]
Balliol College, to which the Boden chair has been attached since university reforms in 1882

Of the other candidates, Cowell was elected as the first Sanskrit professor at the University of Cambridge in 1867, supported by Müller and others.[70] Griffith was principal of his college from 1861 until 1878 (succeeding Ballantyne); he carried out further work in India after his retirement, and died there.[71] Ballantyne resigned as principal because of health problems and returned to England, where he served as librarian to the India Office (a position that Wilson had held in addition to the professorship) until his death in 1864.[7][72]

The academic Jeremy Dibble (in his biography of the composer John Stainer, a friend of Müller) has written that the election "amply foreshadowed the ensuing battle between contemporary sacred and secular forces in the university, the anachronism of Oxford's systems of academic election and the burning need for reform".[73] The Universities of Oxford and Cambridge Act 1877 continued a process of change imposed by Parliament that had begun in the middle of the 19th century, and empowered a group of commissioners to lay down new statutes for the university and its colleges. The commissioners' powers included the ability to rewrite trusts and directions attached to gifts that were 50 years old or more.[74] The statutes governing the Boden chair were revised by the commissioners in 1882; Joseph Boden's original proselytising purpose was no longer mentioned, nor was the professor to be chosen by Convocation.[75][n 4] The commissioners' new statutes for Balliol College in 1881 included a provision that the holder of the Boden professorship was to be appointed as a fellow of the college, creating a link between the chair and Balliol that is still in place.[77][78] As with other professorships, the University Council now makes arrangements for convening a board of electors, upon which Balliol has two representatives, in the event of a vacancy.[79] As of 2017, the Sanskrit professor is Christopher Minkowski, appointed in 2005.[78][80] His predecessor Richard Gombrich has said that he had to "fight a great battle" in 2004 to ensure that another professor was appointed after he retired, and credited his victory to the university's realisation that it was the last chair in Sanskrit left in the United Kingdom.[81]
Notes

At this time, "India" described the area covered by present-day India, Pakistan, Myanmar, Sri Lanka, and Bangladesh.[1]
The letter from Cotton is reproduced in full in Müller, pp. 236–237.
After the election, Müller's wife records that one voter said that if the ballots had been measured by weight, there would have been "no doubt" about the matter.[49]

    Further reforms during the 19th and 20th centuries gradually eroded the powers of Convocation; its only remaining roles are to elect the university's Chancellor and the Professor of Poetry.[76]

References

Beckerlegge, p. 178.
Chichester, H. M.; Carter, Philip (May 2005). "Boden, Joseph (d. 1811)". Oxford Dictionary of National Biography (online ed.). Oxford University Press. doi:10.1093/ref:odnb/2753. Retrieved 9 May 2012. (Subscription or UK public library membership required.)
Beckerlegge, p. 193.
Evison, p. 2.
"Editorial". The Times. 29 October 1860. p. 6. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
Chaudhuri, p. 221.
Courtright, Paul B. (2004). "Wilson, Horace Hayman (1786–1860)". Oxford Dictionary of National Biography (online ed.). Oxford University Press. doi:10.1093/ref:odnb/29657. Retrieved 10 May 2012. (Subscription or UK public library membership required.)
Beckerlegge, p. 186.
Beckerlegge, p. 187.
Beckerlegge, p. 201.
Beckerlegge, p. 202.
Beckerlegge, p. 188.
Dowling, p. 165.
Macdonell, A. A.; Katz, J. B. (October 2007). "Williams, Sir Monier Monier– (1819–1899)". In Katz, J. B (ed.). Oxford Dictionary of National Biography (online ed.). Oxford University Press. doi:10.1093/ref:odnb/18955. Retrieved 14 May 2012. (Subscription or UK public library membership required.)
Kochhar, Rajesh (March–April 2008). "Seductive Orientalism: English Education and Modern Science in Colonial India". Social Scientist. 36 (3/4): 54. JSTOR 27644269.
Van der Veer, p. 109.
Fynes, R. C. C. (May 2007). "Müller, Friedrich Max (1823–1900)". Oxford Dictionary of National Biography (online ed.). Oxford University Press. doi:10.1093/ref:odnb/18394. Retrieved 16 May 2012. (Subscription or UK public library membership required.)
Beckerlegge, p. 180.
Van der Veer, p. 108.
Chaudhuri, p. 220.
"University Intelligence". The Times. 28 May 1860. p. 6. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
"University Intelligence". The Times. 31 October 1860. p. 4. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
"University Intelligence". The Times. 17 August 1860. p. 7. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
"University Intelligence". The Times. 22 November 1860. p. 10. (subscription required)
"Boden Sanscrit Professorship". The Observer. 3 June 1860. p. 3. ProQuest 474988140. (subscription required)
"University Intelligence". The Times. 15 May 1860. p. 9. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
Beckerlegge, pp. 334–335.
Beckerlegge, p. 203.
"University Intelligence". The Times. 16 May 1860. p. 9. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
Beckerlegge, pp. 333–334.
Beckerlegge, p. 197.
Chaudhuri, p. 225.
Beckerlegge, p.198.
Beckerlegge, p. 199.
Chaudhuri, p. 223.
"University Intelligence". The Times. 22 October 1860. p. 7. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
Müller, Max (29 October 1860). "Sanskrit Professorship". The Times. p. 7. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
Chaudhuri, p. 227.
Thomas, p. 85.
Evison, p. 3.
Chaudhuri, p. 222.
Müller, p. 238.
Chaudhuri, p. 226.
"University Intelligence". The Times. 23 May 1860. p. 9. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
Müller, p. 236.
"University Intelligence". The Times. 27 June 1860. p. 12. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
"Boden Professorship of Sanskrit at Oxford". The Times. 5 December 1860. p. 6. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
"Boden Sanskrit Professorship". The Times. 6 December 1860. p. 8. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
Müller, p. 242
Quoted in Beckerlegge, p. 196.
Beckerlegge, p. 196.
Kaul, Chandrika (2003). Reporting the Raj: The British Press and India C. 1880–1922. Manchester University Press. pp. 87–88. ISBN 978-0-7190-6176-9. Archived from the original on 6 December 2021. Retrieved 7 November 2020.
Pusey, Edward (11 June 1860). "The Boden Professorship of Sanskrit". The Times. p. 9. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
Müller, pp. 241–242.
Simpson, R. S. (2004). "Macbride, John David (1778–1868)". Oxford Dictionary of National Biography (online ed.). Oxford University Press. doi:10.1093/ref:odnb/17364. Retrieved 22 May 2012. (Subscription or UK public library membership required.)
Dowling, p. 164.
"University Intelligence". The Times. 8 December 1860. p. 9. Archived from the original on 6 December 2021. Retrieved 21 May 2012.(subscription required)
Tull, Herman W. (June 1991). "F. Max Müller and A. B. Keith: 'Twaddle', the 'Stupid' Myth and the Disease of Indology". Numen. Brill Publishers. 38 (3): 31–32. doi:10.2307/3270003. JSTOR 327003. Part 1.
Beckerlegge, p. 195.
Macdonell, Arthur Anthony (1901). "Obituary: Max Müller". Man. Royal Anthropological Institute of Great Britain and Ireland. 1: 18–23. JSTOR 2840094.
Wheeler-Barclay, Marjorie (2010). The Science of Religion in Britain, 1860–1915. Victorian Literature and Culture. University of Virginia Press. p. 43. ISBN 978-0-8139-3010-7.
Beckerlegge, pp. 202–203.
Müller, p. 244.
Thomas, p. 86.
Beckerlegge, p. 183.
Chaudhuri, pp. 232–234.
Beckerlegge, p. 179.
Dowling, p. 160.
Beckerlegge, p. 173.
Thomas, F. W.; Katz, J. B. (2004). "Cowell, Edward Byles (1826–1903)". In Katz, J. B (ed.). Oxford Dictionary of National Biography (online ed.). Oxford University Press. doi:10.1093/ref:odnb/32595. Retrieved 21 May 2012. (Subscription or UK public library membership required.)
Macdonell, A. A.; Katz, J. B. (2004). "Griffith, Ralph Thomas Hotchkin (1826–1906)". In Katz, J. B (ed.). Oxford Dictionary of National Biography (online ed.). Oxford University Press. doi:10.1093/ref:odnb/33580. Retrieved 21 May 2012. (Subscription or UK public library membership required.)
Simpson, R. S. (2004). "Ballantyne, James Robert (1813–1864)". Oxford Dictionary of National Biography (online ed.). Oxford University Press. doi:10.1093/ref:odnb/1229. Retrieved 22 May 2012. (Subscription or UK public library membership required.)
Dibble, Jeremy (2007). John Stainer: A Life in Music. Boydell Press. p. 128. ISBN 978-1-84383-297-3. Archived from the original on 18 May 2016. Retrieved 23 October 2015.
"Preface: Constitution and Statute-making Powers of the University". University of Oxford. 16 June 2003. Archived from the original on 15 October 2003. Retrieved 22 May 2012.
Statutes, pp. 90–91.
"A history of Congregation and Convocation". Oxford University Archives. 2011. Archived from the original on 22 December 2004. Retrieved 17 May 2012.
Statutes, p. 183 and p. 194.
Burn-Murdoch, Steve (2007). "Boden Professor of Sanskrit". Balliol College, Oxford. Archived from the original on 11 May 2012. Retrieved 4 July 2017.
"Statute XIV: Employment of Academic and Support Staff by the University". University of Oxford. 18 December 2009. Archived from the original on 26 February 2003. Retrieved 25 July 2012.
"Christopher Minkowski". Balliol College, Oxford. 17 February 2016. Archived from the original on 29 February 2016. Retrieved 4 July 2017.

    "Tenth anniversary Board of Governors Dinner". Oxford Centre for Hindu Studies. 25 June 2008. Archived from the original on 24 November 2021. Retrieved 15 May 2012.

Bibliography

    Beckerlegge, Gwilym (1997). "Professor Friedrich Max Müller and the Missionary Cause". In Wolfe, John (ed.). Religion in Victorian Britain. V – Culture and Empire. Manchester University Press. ISBN 0-7190-5184-3. Archived from the original on 25 December 2018. Retrieved 23 October 2015.
    Chaudhuri, Nirad C. (1974). Scholar extraordinary: the life of professor the Rt. Hon. Friedrich Max Muller. Chatto & Windus.
    Dowling, Linda (March 1982). "Victorian Oxford and the Science of Language". Publications of the Modern Language Association of America. Modern Language Association. 97 (2): 160–178. doi:10.2307/462185. JSTOR 462185.
    Evison, Gillian (December 2004). "The Orientalist, his Institute and the Empire: the rise and subsequent decline of Oxford University's Indian Institute" (PDF). Bodleian Library. Archived (PDF) from the original on 4 April 2012. Retrieved 20 May 2012.
    Müller, Georgina, ed. (1902). The life and letters of the Right Honourable Friedrich Max Müller. I. Longmans, Green & Co.
    Statutes made for the University of Oxford, and for the Colleges and Halls therein. Oxford University Press. 1883.
    Thomas, Terence (2000). "Political motivations in the development of the academic studies of religions in Britain". In Geertz, Armin (ed.). Perspectives on Method and Theory in the Study of Religion: Adjunct Proceedings of the XVIIth Congress of the International Association for the History of Religions, Mexico City, 1995. Brill Publishers. ISBN 978-90-04-11877-5. Archived from the original on 2 May 2016. Retrieved 23 October 2015.
    Van der Veer, Peter (2001). Imperial Encounters: Religion and Modernity in India and Britain. Princeton University Press. ISBN 978-0-691-07478-8. Archived from the original on 19 May 2016. Retrieved 23 October 2015.

    vte

Boden Professors of Sanskrit

    Horace Hayman Wilson (1832) 1860 election Monier Monier-Williams (1860) Arthur Anthony Macdonell (1899) Frederick William Thomas (1927) Edward Johnston (1937) Thomas Burrow (1944) Richard Gombrich (1976) Christopher Minkowski (2005)

Portal University of Oxford portal
Categories:

    1860 elections in the United Kingdom1860 in EnglandHistory of the University of OxfordIndia–United Kingdom relationsUniversity and college elections in the United Kingdom19th century in OxfordshireSanskritDecember 1860 eventsNon-partisan electionsElections in Oxford

Navigation menu

    Not logged in
    Talk
    Contributions
    Create account
    Log in

    Article
    Talk

    Read
    Edit
    View history

Search

    Main page
    Contents
    Current events
    Random article
    About Wikipedia
    Contact us
    Donate

Contribute

    Help
    Learn to edit
    Community portal
    Recent changes
    Upload file

Tools

    What links here
    Related changes
    Special pages
    Permanent link
    Page information
    Cite this page
    Wikidata item

Print/export

    Download as PDF
    Printable version

Languages

    العربية

Edit links

    This page was last edited on 6 December 2021, at 20:21 (UTC).
    Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

    Privacy policy
    About Wikipedia
    Disclaimers
    Contact Wikipedia
    Mobile view
    Developers
    Statistics
    Cookie statement

    Wikimedia Foundation
    Powered by MediaWiki

"""


def find_buzzwords(corpus):
    words = corpus.split()
    # print(words)
    words_options = set(words)
    counter = {word: words.count(word) for word in words_options}
    # print(list(counter.items()))
    sorted_buzzwords = sorted(list(counter.items()), key=lambda item: item[1], reverse=True)
    # print(sorted_buzzwords)
    return sorted_buzzwords
    # TODO what about prefixes or close words
    # for word in words:


def get_common_words():
    return stop_words()


def find_unique_buzzwords(corpus):
    all_buzzwords = find_buzzwords(corpus)
    general_common_words = get_common_words()
    uniqe_buzzwords = list()
    for word, freq in all_buzzwords:
        if word not in general_common_words:
            uniqe_buzzwords.append((word, freq))
    return manage_prefixes(uniqe_buzzwords)


_PREF = ['ה', 'ו', 'ב', 'ל', 'ש', 'מ', 'כ', 'וש', 'שה', 'מה', 'לה', 'בה', 'וה']


def manage_prefixes(buzzwords, prefixes=_PREF):
    buzzwords_dict = dict(buzzwords)
    for pref in prefixes:
        for word, freq in buzzwords:

            if pref+word in buzzwords_dict.keys() and word in buzzwords_dict.keys():
                print(word)
                buzzwords_dict[word] += buzzwords_dict[pref+word]
                del buzzwords_dict[pref+word]
    #find only hebrew words
    for key in list(buzzwords_dict.keys()):
        if not any("\u0590" <= c <= "\u05EA" for c in key):
            del buzzwords_dict[key]

    return sorted(list(buzzwords_dict.items()), key=lambda item: item[1], reverse=True)


def stop_words():
    sent = ''
    with open('heb_stop_words.txt', 'r') as f:
        sent = f.read()
    return sent.split()


def main():
    stop_words()
    # Start with one review:
    text = ""

    # Create and generate a word cloud image:
    # wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.plot()
    with open('titles/1.txt', 'r') as f:
        txt = f.read()
    # print(txt)
    unique = find_unique_buzzwords(txt)
    print(unique[:20])


if __name__ == '__main__':
    main()
