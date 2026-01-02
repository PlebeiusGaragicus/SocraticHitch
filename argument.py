from typing import Union, List
from pathlib import Path
from pydantic import HttpUrl
from langchain.schema import AIMessage, HumanMessage
from datetime import datetime

class Analysis:
    """This is AI-generated inference or analysis of the media"""

    prompt: HumanMessage
    """The prompt that was provided to the AI"""

    model: str
    """The model that was used to generate the analysis"""

    reply: AIMessage
    """The reply from the AI"""


class Media:
    """This is a single file (photo, video, csv, etc)"""

    path: Path
    """The path to the media file"""

    ai_analysis: Analysis
    """This is AI-generated inference or analysis of the media"""


class WebResource:
    """This is a single web resource (photo, video, etc) and/or URL"""

    url: HttpUrl
    """The URL of the web resource"""

    timestamp: datetime
    """The timestamp of the web resource"""

    snapshot: Path
    """The PDF snapshot of the web resource"""

    scrape: Media
    """The scrape of the web resource"""

    ai_analysis: Analysis
    """This is AI-generated inference or analysis of the media"""


class Definition:
    """A `Definition` is like a footnote or endnote, and this would be the content or author's remark"""

    term: str
    """A new `term` or `fact` that may later be referrenced in the argument"""

    media: List[Union[Media, WebResource]]
    """A list of media files (photo, video, etc) and/or list of URLs. Perhaps these would be kept in the same 'folder' together."""

    human_narrative: str
    """The content or author's remark regarind the media - this is the 'endnote'"""


class Clause:
    """This is a single-encapsulted "argument" or attempted statement of fact to establish our logic, block by block"""

    title: str
    """the name and unique id of the clause"""

    definitions: List[Definition]
    """our supporting evidence and 'grounding' that establishes meaning and provides point-of-view"""

    narrative: str
    """the body of an argument which pulls from earlier-defined fact"""

    refutation: List[Union[str, Clause, 'SocraticSeminar']]
    """
    - we may have a list of refutations, kept and replied to in order to establish our past thoughts on the issue, old ways of thinking, past contraversies, etc.
    - These can be included to further context to stregnthen our argument.
    - just like how individual Clauses may have a "counter" - if debating on-stage, this would be our interloquitor's counter content and message
    """



class SocraticSeminar:
    """This `Seminar` object defines a cogent argument or `position paper` from an author.  It is the self-contained material for one side in a debate"""

    Abstract: str

    Supporting_Arguments: List[Clause]

    Narrative: Union[Clause]

    Refutations: List[Union[str, Clause, 'SocraticSeminar']]
