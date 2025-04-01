/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { Component, useRef, useState } from "@odoo/owl";
import { CopyClipboardCharField, extractProps } from "@web/views/fields/copy_clipboard/copy_clipboard_field";
import { CopyButton } from "@web/core/copy_button/copy_button";
import { UUIDButton } from "@base_uuid_field/core/uuid_button/uuid_button";
import { CharField } from "@web/views/fields/char/char_field";

export class UUIDField extends CopyClipboardCharField {
    static template = "base_uuid_field.UUIDField";
    static components = { Field: CharField, CopyButton, UUIDButton};
    
    setup() {
        super.setup();
        this.setUUID = this.setUUID.bind(this);
    }

    get uuidSucessText() {
        return _t("Generated")
    }

    get uuidButtonClassName() {
        return this.copyButtonClassName // lazy, but this way we can use the existing css
    }

    get uuidButtonIcon() {
        return "fa-refresh";
    }

    get type() {
        return 'char'; // lazy, but this way we can use the existing css
    }

    async setUUID(uuid) {
        await this.props.record.update({[this.props.name]: uuid})
    }
}

export const uuidField = {
    component: UUIDField,
    displayName: _t("UUID"),
    supportedTypes: ["uuid"],
    extractProps
};

registry.category("fields").add("uuid", uuidField);