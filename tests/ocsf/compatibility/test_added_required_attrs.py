

from ocsf.schema import OcsfAttr
from ocsf.compare import ChangedSchema, ChangedEvent, ChangedObject, ChangedAttr, Addition
from ocsf.validate.compatibility.added_required_attrs import AddedRequiredAttrFinding, NoAddedRequiredAttrsRule


def test_added_required_attr_event():
    """Test that the rule finds an added required attribute in an event."""
    s = ChangedSchema(
        classes={
            "process_activity": ChangedEvent(
                attributes={
                    "process_name": Addition(OcsfAttr(caption="", type="str_t", requirement="required")),
                }
            ),
        }
    )

    rule = NoAddedRequiredAttrsRule()
    findings = rule.validate(s)
    assert len(findings) == 1
    assert isinstance(findings[0], AddedRequiredAttrFinding)


def test_added_required_attr_object():
    """Test that the rule finds an added required attribute in an object."""
    s = ChangedSchema(
        objects={
            "process": ChangedObject(
                attributes={
                    "process_name": Addition(OcsfAttr(caption="", type="str_t", requirement="required")),
                }
            ),
        }
    )

    rule = NoAddedRequiredAttrsRule()
    findings = rule.validate(s)
    assert len(findings) == 1
    assert isinstance(findings[0], AddedRequiredAttrFinding)