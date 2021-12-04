import json

from odoo import _, models
from odoo.exceptions import UserError


class ReSequenceWizard(models.TransientModel):
    _inherit = "account.resequence.wizard"

    def resequence(self):
        new_values = json.loads(self.new_values)
        # Can't change the name of a posted invoice, but we do not want to have the chatter
        # logging 3 separate changes with [state to draft], [change of name], [state to posted]
        if (
            self.move_ids.journal_id
            and self.move_ids.journal_id.restrict_mode_hash_table
        ):
            raise UserError(
                _(
                    "You can not reorder sequence when the journal is locked with a hash."
                )
            )
        self.with_context(tracking_disable=True).move_ids.state = "draft"
        for move_id in self.move_ids:
            if str(move_id.id) in new_values:
                if self.ordering == "keep":
                    move_id.name = new_values[str(move_id.id)]["new_by_name"]
                else:
                    move_id.name = new_values[str(move_id.id)]["new_by_date"]
                move_id.with_context(tracking_disable=True).state = new_values[
                    str(move_id.id)
                ]["state"]
