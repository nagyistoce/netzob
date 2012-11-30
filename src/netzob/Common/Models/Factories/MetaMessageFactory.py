# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Standard library imports
#+---------------------------------------------------------------------------+
import uuid

#+---------------------------------------------------------------------------+
#| Related third party imports
#+---------------------------------------------------------------------------+
from lxml.etree import ElementTree
from netzob.Common.Type.TypeConvertor import TypeConvertor
from netzob.Common.Token import Token
from lxml import etree

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+
from netzob.Common.Type.Format import Format


#+---------------------------------------------------------------------------+
#| MetaMessageFactory:
#|     Factory dedicated to the manipulation of meta messages
#+---------------------------------------------------------------------------+
class MetaMessageFactory(object):
    """Factory dedicated to the manipulation of meta messages. Meta messages allows
    applications to generate XML messages with custom attribute data."""

    XML_SCHEMA_TYPE = "netzob-common:MetaMessage"

    @staticmethod
    def save(message, xmlMessage, namespace_project, namespace_common):
        """Generate the XML representation of a Meta message"""

        xmlMessage.set("{http://www.w3.org/2001/XMLSchema-instance}type", MetaMessageFactory.XML_SCHEMA_TYPE)

        attributes = message.getAttributes()

        for a in attributes:
            subElement = etree.SubElement(xmlMessage, "{" + namespace_common + "}attribute", name=a[0], type=a[1])
            subElement.text = str(a[2])

    @staticmethod
    def loadFromXML(rootElement, namespace, version, id, timestamp, data):
        """Function which parses an XML and extract from it
           the definition of a meta message
           @param rootElement: XML root of the meta message
           @return an instance of a MetaMessage
           @raise NameError if XML invalid"""

        if rootElement.get("{http://www.w3.org/2001/XMLSchema-instance}type", "abstract") != MetaMessageFactory.XML_SCHEMA_TYPE:
            raise NameError("The parsed xml doesn't represent a Meta message.")

        attributes = []

        for a in rootElement.iter("{" + namespace + "}attribute"):
            if a.attrib['type'] not in Format.getExtendedSupportedFormats():
                raise NameError("The attribute type has an unsupported value.")

            attributes.append([a.attrib['name'], a.attrib['type'], a.text])

        # TODO : verify this ! Circular imports in python !
        # WARNING : verify this ! Circular imports in python !
        from netzob.Common.Models.MetaMessage import MetaMessage
        result = MetaMessage(id, timestamp, data, attributes)

        return result
