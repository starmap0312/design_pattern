import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from abc import ABCMeta, abstractmethod

class Stamp(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def attach(self, msg):
        pass

class Enclosure(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def part(self):
        pass

class Wire(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def connect(self):
        pass

class Envelope(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def unwrap(self):
        pass

class SMTP(Wire):

    def __init__(self, server):
        self.server = server

    def connect(self):
        return smtplib.SMTP(self.server)

class Address(object):

    def __init__(self, addr, name=None):
        self.addr = addr
        self.name = name

    def to_string(self):
        return '{0} <{1}>'.format(self.name, self.addr) if self.name else self.addr

class EnPlain(Enclosure):

    def __init__(self, content):
        self.content = content

    def part(self):
        return MIMEText(self.content, 'plain')

class EnHTML(Enclosure):

    def __init__(self, content):
        self.content = content

    def part(self):
        return MIMEText(self.content, 'html')

class StSender(Stamp):

    def __init__(self, address):
        self.address = address

    def attach(self, msg):
        msg['From'] = self.address.to_string()

class StRecipient(Stamp):

    def __init__(self, address):
        self.address = address

    def attach(self, msg):
        msg['To'] = self.address.to_string()

class StSubject(Stamp):

    def __init__(self, subject):
        self.subject = subject

    def attach(self, msg):
        msg['Subject'] = self.subject

class DefaultEnvelope(Envelope):

    def __init__(self, stamps, enclosures):
        self.stamps = stamps
        self.enclosures = enclosures

    def unwrap(self):
        msg = MIMEMultipart('alternative')
        for enclosure in self.enclosures:
            msg.attach(enclosure.part())
        for stamp in self.stamps:
            stamp.attach(msg)
        return msg

class Postman(object):

    def __init__(self, wire):
        self.wire = wire

    def send(self, envelope):
        smtp = self.wire.connect()
        msg = envelope.unwrap()
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())

if __name__ == '__main__':
    postman = Postman(SMTP('example.relay.com'))
    postman.send(
        DefaultEnvelope(
            [
                StSender(Address("kuanyu@yahoo-inc.com", "Kuan-Yu Chen")),
                StRecipient(Address("kuanyu@yahoo-inc.com")),
                StSubject("subject")
            ],
            [
                EnPlain("plain text"),
                EnHTML("<html><p>html text</p></html>")
            ]
        )
    )
