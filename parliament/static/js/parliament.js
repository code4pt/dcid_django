function confirm_delete(proposal_id) {
    var answer = confirm("Do you want to delete your proposal for ever?")
    if (answer) {
        //TODO Proposal.objects.get(pk=proposal_id).delete();        
        window.location = "/parliament/proposals/";
    }
}