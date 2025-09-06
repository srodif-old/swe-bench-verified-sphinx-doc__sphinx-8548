"""Test for inherited attributes documentation."""

import pytest

from .test_ext_autodoc import do_autodoc


@pytest.mark.sphinx('html', testroot='ext-autodoc')
def test_autodoc_inherited_attributes(app):
    """Test that inherited attributes are documented when using inherited-members."""
    options = {"members": None,
               "inherited-members": None}
    actual = do_autodoc(app, 'class', 'target.inherited_attributes.DerivedClass', options)
    
    # Should contain the inherited base_attr from BaseClass
    assert '.. py:attribute:: DerivedClass.base_attr' in actual
    # Should also contain its own derived_attr
    assert '.. py:attribute:: DerivedClass.derived_attr' in actual


@pytest.mark.sphinx('html', testroot='ext-autodoc')
def test_autodoc_inherited_attributes_no_inherited_members(app):
    """Test that inherited attributes are NOT documented when NOT using inherited-members."""
    options = {"members": None}
    actual = do_autodoc(app, 'class', 'target.inherited_attributes.DerivedClass', options)
    
    # Should NOT contain the inherited base_attr from BaseClass
    assert '.. py:attribute:: DerivedClass.base_attr' not in actual
    # Should contain its own derived_attr
    assert '.. py:attribute:: DerivedClass.derived_attr' in actual