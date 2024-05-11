from ..interfaces import Processor


class ProcessedContext:
    """
    This class is used to store the processed data and the processors used to process it.
    The `processed` attribute is a dictionary that contains the processors used to process the data.

    Additionally, keyword arguments can be passed to the constructor to initialize the data.

    The `generated` method is used to process the data and return the final result.
    
    The processors are applied in the order they are defined in the list. The result of the 
    previous processor is passed to the next one.
    """
    data: dict
    processed: dict[str, list[Processor]]

    def __init__(self, processed: dict[str, list[Processor]], context: dict = {}):
        self.data = context
        self.processed = processed

    def generate(self) -> dict:
        for key, processors in self.processed.items():
            current = None
            for processor in processors:
                current = processor.process(current, key, self.data)
                
            self.data[key] = current
        return self.data