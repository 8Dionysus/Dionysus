<a id="titan-compaction-recovery"></a>

# Seed: Titan Compaction Recovery v0 {#titan-compaction-recovery}

Compaction-recovered dossiers may restore visible dialogue but not perfect command chronology.

Replay and memory records produced from such sources must include:
source_kind = compaction_recovered_message_history
chronology_confidence = message_order_only
tool_trace_available = after_recovery_boundary | partial | unavailable
